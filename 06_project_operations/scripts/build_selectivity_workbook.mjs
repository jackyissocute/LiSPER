#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";
import { FileBlob, SpreadsheetFile, Workbook } from "@oai/artifact-tool";


const root = process.cwd();
const rawRoot = path.join(root, "01_computational_discovery/data/raw");
const outputDir = path.join(root, "01_computational_discovery/data/processed");
const previewDir = "/tmp/lisper_selectivity_workbook_previews";

function parseTsv(text) {
  const lines = text.trim().split(/\r?\n/);
  const headers = lines[0].split("\t");
  return lines.slice(1).filter(Boolean).map((line) => Object.fromEntries(headers.map((header, index) => [header, line.split("\t")[index] ?? ""])));
}

function parseXvg(text) {
  return text.split(/\r?\n/).filter((line) => line && !"#@".includes(line[0])).map((line) => line.trim().split(/\s+/).map(Number)).filter((row) => row.length >= 2 && row.every(Number.isFinite));
}

function numeric(value) {
  return value === "" ? null : Number(value);
}

function meanRegion(points, lo, hi) {
  const values = points.filter(([x]) => x >= lo && x <= hi).map(([, y]) => y);
  if (!values.length) throw new Error(`No profile bins in ${lo}–${hi} nm`);
  return values.reduce((sum, value) => sum + value, 0) / values.length;
}

function calculateEstimate(profileRows, bootstrapRows, bounds) {
  const [boundMin, boundMax, refMin, refMax] = bounds;
  const corrected = profileRows.map(([x, y]) => [x, y + 0.00831446261815324 * 298.15 * Math.log(4 * Math.PI * x ** 2)]);
  const deltaG = meanRegion(corrected, boundMin, boundMax) - meanRegion(corrected, refMin, refMax);
  const boundSd = meanRegion(bootstrapRows.map(([x, , sd]) => [x, sd]), boundMin, boundMax);
  const refSd = meanRegion(bootstrapRows.map(([x, , sd]) => [x, sd]), refMin, refMax);
  return { deltaG, uncertainty: Math.hypot(boundSd, refSd) };
}

function setHeader(sheet, range) {
  sheet.getRange(range).format = {
    fill: "#17365D",
    font: { bold: true, color: "#FFFFFF" },
    rowHeight: 24,
    verticalAlignment: "center",
    wrapText: true,
    borders: { preset: "outside", style: "thin", color: "#17365D" },
  };
}

function finishSheet(sheet, freezeRows = 1) {
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(freezeRows);
}

function addTable(sheet, range, name) {
  const table = sheet.tables.add(range, true, name);
  table.style = "TableStyleMedium2";
  table.showBandedRows = true;
  table.showFilterButton = true;
  return table;
}

const deltaRows = parseTsv(await fs.readFile(path.join(rawRoot, "pmf/summary/delta_g_summary.tsv"), "utf8"));
const selectivityRows = parseTsv(await fs.readFile(path.join(rawRoot, "pmf/summary/selectivity_summary.tsv"), "utf8"));
const manifestRows = parseTsv(await fs.readFile(path.join(rawRoot, "source_manifest.tsv"), "utf8"));
if (deltaRows.length !== 16 || selectivityRows.length !== 8 || manifestRows.length !== 244) throw new Error("Unexpected curated source dimensions");
const conditionMap = new Map(deltaRows.map((row) => [`${row.candidate}|${row.condition}`, row]));
const calculatedMap = new Map();
for (const row of selectivityRows) {
  const li = conditionMap.get(`${row.candidate}|LiCl`);
  const na = conditionMap.get(`${row.candidate}|NaCl`);
  if (!li || !na) throw new Error(`Missing paired condition for ${row.candidate}`);
  if (Math.abs((Number(li.delta_g_kjmol) - Number(na.delta_g_kjmol)) - Number(row.delta_delta_g_kjmol)) > 0.002) throw new Error(`ΔΔG mismatch for ${row.candidate}`);
  if (Math.abs(Math.hypot(Number(li.bootstrap_unc_kjmol), Number(na.bootstrap_unc_kjmol)) - Number(row.bootstrap_unc_ddg_kjmol)) > 0.002) throw new Error(`Uncertainty mismatch for ${row.candidate}`);
  const bounds = [row.bound_min_nm, row.bound_max_nm, row.ref_min_nm, row.ref_max_nm].map(Number);
  for (const condition of ["LiCl", "NaCl"]) {
    const folder = path.join(rawRoot, `pmf/${row.candidate}/${condition}`);
    const estimate = calculateEstimate(
      parseXvg(await fs.readFile(path.join(folder, "profile_full.xvg"), "utf8")),
      parseXvg(await fs.readFile(path.join(folder, "bootstrap_std.xvg"), "utf8")),
      bounds,
    );
    const reported = conditionMap.get(`${row.candidate}|${condition}`);
    if (Math.abs(estimate.deltaG - Number(reported.delta_g_kjmol)) > 0.0015) throw new Error(`Recomputed ΔG mismatch for ${row.candidate} ${condition}`);
    if (Math.abs(estimate.uncertainty - Number(reported.bootstrap_unc_kjmol)) > 0.0015) throw new Error(`Recomputed uncertainty mismatch for ${row.candidate} ${condition}`);
    calculatedMap.set(`${row.candidate}|${condition}`, estimate);
  }
}

const workbook = Workbook.create();
const selectivity = workbook.worksheets.add("Selectivity");
const conditions = workbook.worksheets.add("Condition Results");
const qc = workbook.worksheets.add("QC Diagnostics");
const profiles = workbook.worksheets.add("PMF Profiles");
const parameters = workbook.worksheets.add("Parameters");
const provenance = workbook.worksheets.add("Provenance");

// Selectivity: reported condition inputs with formula-driven paired differences.
selectivity.getRange("A1:I1").values = [[
  "Candidate", "ΔG Li (kJ/mol)", "Bootstrap SD Li (kJ/mol)", "ΔG Na (kJ/mol)", "Bootstrap SD Na (kJ/mol)",
  "ΔΔG Li−Na (kJ/mol)", "Propagated SD (kJ/mol)", "Nominal preference", "Status",
]];
const selectivityValues = selectivityRows.map((row) => {
  const li = calculatedMap.get(`${row.candidate}|LiCl`);
  const na = calculatedMap.get(`${row.candidate}|NaCl`);
  return [row.candidate, li.deltaG, li.uncertainty, na.deltaG, na.uncertainty, null, null, null, row.status];
});
selectivity.getRange(`A2:I${selectivityValues.length + 1}`).values = selectivityValues;
selectivity.getRange("F2:H2").formulas = [["=B2-D2", "=SQRT(C2^2+E2^2)", '=IF(F2<0,"Li",IF(F2>0,"Na","Equal"))']];
selectivity.getRange("F2:H9").fillDown();
selectivity.getRange("B2:G9").format.numberFormat = "0.000";
selectivity.getRange("A1:A9").format.columnWidth = 18;
selectivity.getRange("B1:G9").format.columnWidth = 18;
selectivity.getRange("H1:H9").format.columnWidth = 12;
selectivity.getRange("I1:I9").format.columnWidth = 18;
selectivity.getRange("A2:I9").format.borders = { insideVertical: { style: "thin", color: "#D9E2F3" } };
selectivity.getRange("F2:F9").conditionalFormats.add("cellIs", { operator: "lessThan", formula: 0, format: { fill: "#D9EAF7", font: { color: "#005B96" } } });
selectivity.getRange("F2:F9").conditionalFormats.add("cellIs", { operator: "greaterThan", formula: 0, format: { fill: "#FCE4D6", font: { color: "#9C4100" } } });
setHeader(selectivity, "A1:I1");
addTable(selectivity, "A1:I9", "SelectivityTable");
finishSheet(selectivity);

// Condition-level reported estimates and diagnostics.
const conditionHeaders = [
  "Candidate", "Condition", "ΔG (kJ/mol)", "Bootstrap SD (kJ/mol)", "Endpoint span (kJ/mol)",
  "Early−late difference (kJ/mol)", "Burn-in max shift (kJ/mol)", "Histogram min support", "Histogram weak bins",
  "IACT min (ps)", "IACT median (ps)", "IACT max (ps)", "Status",
];
conditions.getRange("A1:M1").values = [conditionHeaders];
conditions.getRange("A2:M17").values = deltaRows.map((row) => [
  row.candidate, row.condition, numeric(row.delta_g_kjmol), numeric(row.bootstrap_unc_kjmol), numeric(row.endpoint_span_kjmol),
  numeric(row.early_late_difference_kjmol), numeric(row.burnin_max_shift_kjmol), numeric(row.histogram_min_support), numeric(row.histogram_weak_bins),
  numeric(row.iact_min_ps), numeric(row.iact_median_ps), numeric(row.iact_max_ps), row.status,
]);
conditions.getRange("C2:G17").format.numberFormat = "0.000";
conditions.getRange("H2:I17").format.numberFormat = "0";
conditions.getRange("J2:L17").format.numberFormat = "0.000";
conditions.getRange("A1:A17").format.columnWidth = 18;
conditions.getRange("B1:B17").format.columnWidth = 12;
conditions.getRange("C1:G17").format.columnWidth = 18;
conditions.getRange("H1:I17").format.columnWidth = 17;
conditions.getRange("J1:L17").format.columnWidth = 16;
conditions.getRange("M1:M17").format.columnWidth = 18;
conditions.getRange("A2:M17").format.borders = { insideVertical: { style: "thin", color: "#D9E2F3" } };
setHeader(conditions, "A1:M1");
addTable(conditions, "A1:M17", "ConditionResultsTable");
finishSheet(conditions);

// Paired QC values preserve the detailed audit fields from each candidate.
const qcFields = [
  "candidate", "status", "temperature_k", "delta_delta_g_kjmol", "bootstrap_unc_ddg_kjmol", "endpoint_span_li_kjmol",
  "endpoint_span_na_kjmol", "half_difference_li_kjmol", "half_difference_na_kjmol", "burnin_max_shift_li_kjmol",
  "burnin_max_shift_na_kjmol", "histogram_min_support_li", "histogram_min_support_na", "iact_max_li_ps", "iact_max_na_ps",
];
const qcHeaders = [
  "Candidate", "Status", "Temperature (K)", "ΔΔG", "Propagated SD", "Endpoint span Li", "Endpoint span Na",
  "Early−late Li", "Early−late Na", "Burn-in shift Li", "Burn-in shift Na", "Histogram support Li", "Histogram support Na",
  "Max IACT Li", "Max IACT Na",
];
const qcRows = [];
for (const summary of selectivityRows) {
  const rows = parseTsv(await fs.readFile(path.join(rawRoot, `pmf/${summary.candidate}/paired_qc.tsv`), "utf8"));
  if (rows.length !== 1) throw new Error(`Unexpected QC rows for ${summary.candidate}`);
  qcRows.push(qcFields.map((field, index) => index < 2 ? rows[0][field] : numeric(rows[0][field])));
}
qc.getRange("A1:O1").values = [qcHeaders];
qc.getRange("A2:O9").values = qcRows;
qc.getRange("C2:O9").format.numberFormat = "0.000";
qc.getRange("L2:M9").format.numberFormat = "0";
qc.getRange("A1:A9").format.columnWidth = 18;
qc.getRange("B1:B9").format.columnWidth = 18;
qc.getRange("C1:O9").format.columnWidth = 16;
qc.getRange("A2:O9").format.borders = { insideVertical: { style: "thin", color: "#D9E2F3" } };
setHeader(qc, "A1:O1");
addTable(qc, "A1:O9", "QCDiagnosticsTable");
finishSheet(qc);

// Parameters and locked analysis regions.
parameters.getRange("A1:B3").values = [["Parameter", "Value"], ["Gas constant (kJ mol⁻¹ K⁻¹)", 0.00831446261815324], ["Temperature (K)", 298.15]];
parameters.getRange("A5:E5").values = [["Candidate", "Bound min (nm)", "Bound max (nm)", "Reference min (nm)", "Reference max (nm)"]];
parameters.getRange("A6:E13").values = selectivityRows.map((row) => [row.candidate, numeric(row.bound_min_nm), numeric(row.bound_max_nm), numeric(row.ref_min_nm), numeric(row.ref_max_nm)]);
parameters.getRange("B2:B3").format.numberFormat = "0.000000000000";
parameters.getRange("B6:E13").format.numberFormat = "0.0000";
parameters.getRange("A1:A13").format.columnWidth = 31;
parameters.getRange("B1:E13").format.columnWidth = 20;
setHeader(parameters, "A1:B1");
setHeader(parameters, "A5:E5");
addTable(parameters, "A1:B3", "ConstantsTable");
addTable(parameters, "A5:E13", "RegionsTable");
parameters.showGridLines = false;
parameters.freezePanes.freezeRows(1);

// Flat PMF table with formula-derived radial correction and reference centering.
profiles.getRange("A1:H1").values = [[
  "Candidate", "Condition", "Distance (nm)", "Raw PMF (kJ/mol)", "Radial correction (kJ/mol)",
  "Corrected PMF (kJ/mol)", "Reference mean (kJ/mol)", "PMF−reference mean (kJ/mol)",
]];
const profileValues = [];
const profileFormulas = [];
let profileRow = 2;
for (const summary of selectivityRows) {
  for (const condition of ["LiCl", "NaCl"]) {
    const sourceRows = parseXvg(await fs.readFile(path.join(rawRoot, `pmf/${summary.candidate}/${condition}/profile_full.xvg`), "utf8"));
    if (sourceRows.length !== 200) throw new Error(`Unexpected profile length for ${summary.candidate} ${condition}`);
    const startRow = profileRow;
    const refIndexes = sourceRows.map((row, index) => ({ distance: row[0], index })).filter(({ distance }) => distance >= Number(summary.ref_min_nm) && distance <= Number(summary.ref_max_nm)).map(({ index }) => index);
    if (!refIndexes.length) throw new Error(`No reference bins for ${summary.candidate} ${condition}`);
    const refStart = startRow + refIndexes[0];
    const refEnd = startRow + refIndexes.at(-1);
    for (const row of sourceRows) {
      profileValues.push([summary.candidate, condition, row[0], row[1]]);
      profileFormulas.push([
        `='Parameters'!$B$2*'Parameters'!$B$3*LN(4*PI()*C${profileRow}^2)`,
        `=D${profileRow}+E${profileRow}`,
        `=AVERAGE($F$${refStart}:$F$${refEnd})`,
        `=F${profileRow}-G${profileRow}`,
      ]);
      profileRow += 1;
    }
  }
}
const profileEnd = profileRow - 1;
profiles.getRange(`A2:D${profileEnd}`).values = profileValues;
profiles.getRange(`E2:H${profileEnd}`).formulas = profileFormulas;
profiles.getRange(`C2:H${profileEnd}`).format.numberFormat = "0.000000";
profiles.getRange(`A1:A${profileEnd}`).format.columnWidth = 18;
profiles.getRange(`B1:B${profileEnd}`).format.columnWidth = 12;
profiles.getRange(`C1:H${profileEnd}`).format.columnWidth = 21;
profiles.getRange(`A2:H${profileEnd}`).format.borders = { insideVertical: { style: "thin", color: "#D9E2F3" } };
setHeader(profiles, "A1:H1");
addTable(profiles, `A1:H${profileEnd}`, "PMFProfilesTable");
finishSheet(profiles);

// File-level provenance and hashes.
provenance.getRange("A1:E1").values = [["Curated path", "Source path", "Bytes", "SHA-256", "Role"]];
provenance.getRange(`A2:E${manifestRows.length + 1}`).values = manifestRows.map((row) => [row.curated_path, row.source_path, numeric(row.bytes), row.sha256, row.role]);
provenance.getRange(`C2:C${manifestRows.length + 1}`).format.numberFormat = "#,##0";
provenance.getRange(`A1:A${manifestRows.length + 1}`).format.columnWidth = 58;
provenance.getRange(`B1:B${manifestRows.length + 1}`).format.columnWidth = 72;
provenance.getRange(`C1:C${manifestRows.length + 1}`).format.columnWidth = 14;
provenance.getRange(`D1:D${manifestRows.length + 1}`).format.columnWidth = 66;
provenance.getRange(`E1:E${manifestRows.length + 1}`).format.columnWidth = 20;
provenance.getRange(`A2:B${manifestRows.length + 1}`).format.wrapText = true;
provenance.getRange(`A2:E${manifestRows.length + 1}`).format.rowHeight = 34;
provenance.getRange(`A2:E${manifestRows.length + 1}`).format.verticalAlignment = "top";
provenance.getRange(`A2:E${manifestRows.length + 1}`).format.borders = { insideVertical: { style: "thin", color: "#D9E2F3" } };
setHeader(provenance, "A1:E1");
addTable(provenance, `A1:E${manifestRows.length + 1}`, "ProvenanceTable");
finishSheet(provenance);

await fs.mkdir(previewDir, { recursive: true });
const previewRanges = {
  Selectivity: "A1:I9",
  "Condition Results": "A1:M17",
  "QC Diagnostics": "A1:O9",
  "PMF Profiles": "A1:H28",
  Parameters: "A1:E13",
  Provenance: "A1:E18",
};
for (const [sheetName, range] of Object.entries(previewRanges)) {
  const preview = await workbook.render({ sheetName, range, scale: 1.25, format: "png" });
  await fs.writeFile(path.join(previewDir, `${sheetName.replaceAll(" ", "_")}.png`), new Uint8Array(await preview.arrayBuffer()));
}

const keyCheck = await workbook.inspect({ kind: "table", range: "Selectivity!A1:I9", include: "values,formulas", tableMaxRows: 10, tableMaxCols: 10, maxChars: 6000 });
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "final formula error scan", maxChars: 3000 });
console.log(keyCheck.ndjson);
console.log(errors.ndjson);

await fs.mkdir(outputDir, { recursive: true });
const output = await SpreadsheetFile.exportXlsx(workbook);
const outputPath = path.join(outputDir, "selectivity_analysis.xlsx");
await output.save(outputPath);
const reloaded = await SpreadsheetFile.importXlsx(await FileBlob.load(outputPath));
const reloadCheck = await reloaded.inspect({ kind: "table", range: "Selectivity!A1:I9", include: "values,formulas", tableMaxRows: 10, tableMaxCols: 10, maxChars: 6000 });
const reloadErrors = await reloaded.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 300 }, summary: "post-export formula error scan", maxChars: 3000 });
console.log(reloadCheck.ndjson);
console.log(reloadErrors.ndjson);
console.log(`workbook=${outputPath} profiles=${profileValues.length} provenance=${manifestRows.length}`);
