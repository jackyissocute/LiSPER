#!/usr/bin/env python3
"""Generate pET-28a(+) vendor plasmid files from IDT codon-optimized CSV exports."""

from __future__ import annotations

import csv
import re
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import CompoundLocation, FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
from snapgene_reader import snapgene_file_to_dict


ROOT = Path(__file__).resolve().parents[1]
INPUT_TSV = ROOT / "sequences" / "candidates.tsv"
VECTOR_DNA = ROOT / "plasmids" / "vector_maps" / "pET28a_plus.dna"
OUTDIR = ROOT / "plasmids" / "vendor_ready_pet28a_idt"
GB_DIR = OUTDIR / "genbank"
IDT_EXPORT_DIR = OUTDIR / "idt_optimizer_exports"

VECTOR = "pET-28a(+)"
ANTIBIOTIC = "Kanamycin"
PROMOTER = "T7 promoter"
STOP_CODON = "TAA"
N_TERMINAL_LEADER = "MGSSHHHHHHSSGLVPRGSHMASMTGGQQMGRGS"

# Zero-based half-open coordinates from the local pET-28a(+) SnapGene file.
# The expression cassette is on the reverse strand in this vector map.
MCS_AFTER_BAMHI_START = 157
MCS_AFTER_BAMHI_END = 197
RETAINED_BAMHI_START = 197
RETAINED_BAMHI_END = 203
ATG_END_OLD = 299

RESTRICTION_SITES = {
    "NcoI": "CCATGG",
    "NdeI": "CATATG",
    "XhoI": "CTCGAG",
    "BamHI": "GGATCC",
    "EcoRI": "GAATTC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "SacI": "GAGCTC",
    "SalI": "GTCGAC",
}


def read_candidates() -> list[dict[str, str]]:
    with INPUT_TSV.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def idt_export_path(candidate_id: str) -> Path:
    return IDT_EXPORT_DIR / f"{candidate_id}_idt_optimized.csv"


def read_idt_sequence(path: Path) -> str:
    with path.open(newline="") as handle:
        row = next(csv.DictReader(handle))
    normalized = {key.strip(): value.strip() for key, value in row.items()}
    dna = re.sub(r"[^ACGTacgt]", "", normalized["Full Sequence"]).upper()
    if not dna:
        raise ValueError(f"No DNA sequence found in {path}")
    return dna


def translate_dna(dna: str) -> str:
    return str(Seq(dna).translate(to_stop=False)).rstrip("*")


def find_sites(sequence: str) -> dict[str, list[int]]:
    sites: dict[str, list[int]] = {}
    for enzyme, motif in RESTRICTION_SITES.items():
        starts = [match.start() + 1 for match in re.finditer(f"(?={motif})", sequence)]
        if starts:
            sites[enzyme] = starts
    return sites


def mapped_coord(old_pos: int, insert_len: int) -> int:
    delta = insert_len - (MCS_AFTER_BAMHI_END - MCS_AFTER_BAMHI_START)
    if old_pos < MCS_AFTER_BAMHI_START:
        return old_pos
    if old_pos >= MCS_AFTER_BAMHI_END:
        return old_pos + delta
    raise ValueError(f"Old coordinate {old_pos} lies in replaced MCS segment")


def feature(start: int, end: int, strand: int | None, ftype: str, label: str, **quals) -> SeqFeature:
    qualifiers = {"label": label}
    qualifiers.update({key: value for key, value in quals.items() if value is not None})
    return SeqFeature(FeatureLocation(start, end, strand=strand), type=ftype, qualifiers=qualifiers)


def wrap_origin_feature(
    start: int,
    end: int,
    strand: int | None,
    ftype: str,
    label: str,
    seq_len: int,
    **quals,
) -> SeqFeature:
    qualifiers = {"label": label}
    qualifiers.update({key: value for key, value in quals.items() if value is not None})
    if start <= end:
        loc = FeatureLocation(start, end, strand=strand)
    else:
        loc = CompoundLocation(
            [
                FeatureLocation(start, seq_len, strand=strand),
                FeatureLocation(0, end, strand=strand),
            ]
        )
    return SeqFeature(loc, type=ftype, qualifiers=qualifiers)


def make_record(
    plasmid_name: str,
    candidate_id: str,
    amino_acids: str,
    idt_dna: str,
    idt_source_file: str,
    vector_seq: str,
) -> tuple[SeqRecord, dict[str, str]]:
    insert_expression = idt_dna + STOP_CODON
    insert_rc = str(Seq(insert_expression).reverse_complement())
    new_seq = vector_seq[:MCS_AFTER_BAMHI_START] + insert_rc + vector_seq[MCS_AFTER_BAMHI_END:]
    insert_len = len(insert_rc)
    seq_len = len(new_seq)

    candidate_start = MCS_AFTER_BAMHI_START
    candidate_end = candidate_start + insert_len
    retained_bamhi_start = mapped_coord(RETAINED_BAMHI_START, insert_len)
    retained_bamhi_end = mapped_coord(RETAINED_BAMHI_END, insert_len)
    tag_start = mapped_coord(RETAINED_BAMHI_START, insert_len)
    tag_end = mapped_coord(ATG_END_OLD, insert_len)
    expression_region = str(Seq(new_seq[candidate_start:tag_end]).reverse_complement())
    full_translation = translate_dna(expression_region)
    expected_full = N_TERMINAL_LEADER + amino_acids

    record = SeqRecord(
        Seq(new_seq),
        id=plasmid_name,
        name=plasmid_name[:16],
        description=f"{plasmid_name}: IDT-optimized {candidate_id} in pET-28a(+) N-terminal His/T7 frame",
    )
    record.annotations["molecule_type"] = "DNA"
    record.annotations["topology"] = "circular"
    record.annotations["data_file_division"] = "SYN"
    record.annotations["date"] = "14-JUN-2026"

    delta = insert_len - (MCS_AFTER_BAMHI_END - MCS_AFTER_BAMHI_START)
    record.features = [
        wrap_origin_feature(25, 73, -1, "terminator", "T7 terminator", seq_len),
        feature(694 + delta, 772 + delta, 1, "promoter", "lacI promoter"),
        feature(772 + delta, 1855 + delta, 1, "CDS", "lacI", gene="lacI", product="lac repressor"),
        feature(2663 + delta, 2855 + delta, 1, "CDS", "rop", gene="rop", product="Rop protein"),
        feature(3284 + delta, 3873 + delta, -1, "rep_origin", "ori"),
        feature(3994 + delta, 4810 + delta, 1, "CDS", "KanR", gene="aph(3')-Ia", product="kanamycin resistance protein"),
        feature(4902 + delta, 5358 + delta, -1, "rep_origin", "f1 ori"),
        feature(mapped_coord(367, insert_len), mapped_coord(386, insert_len), -1, "promoter", "T7 promoter"),
        feature(mapped_coord(342, insert_len), mapped_coord(367, insert_len), None, "protein_bind", "lac operator", bound_moiety="lac repressor"),
        feature(mapped_coord(306, insert_len), mapped_coord(312, insert_len), -1, "RBS", "RBS"),
        feature(tag_start, tag_end, -1, "CDS", "N-terminal His/T7 leader", product="N-terminal pET-28a(+) His/T7 leader", translation=N_TERMINAL_LEADER),
        feature(mapped_coord(269, insert_len), mapped_coord(287, insert_len), -1, "CDS", "6xHis", product="N-terminal 6xHis affinity tag", translation="HHHHHH"),
        feature(mapped_coord(242, insert_len), mapped_coord(260, insert_len), -1, "CDS", "thrombin site", product="thrombin recognition site", translation="LVPRGS"),
        feature(mapped_coord(206, insert_len), mapped_coord(239, insert_len), -1, "CDS", "T7 tag", product="T7 epitope tag", translation="MASMTGGQQMG"),
        feature(retained_bamhi_start, retained_bamhi_end, -1, "misc_feature", "retained BamHI GS linker", note="BamHI-derived Gly-Ser linker retained upstream of insert"),
        feature(candidate_start, candidate_end, -1, "CDS", candidate_id, gene=candidate_id, product=f"{candidate_id} IDT-optimized candidate insert", translation=amino_acids, note=f"IDT source file: {idt_source_file}"),
        feature(candidate_start, candidate_start + 3, -1, "misc_feature", "stop codon", note="TAA stop codon after candidate insert prevents C-terminal vector tag expression"),
    ]

    site_summary = "; ".join(f"{enzyme}:{','.join(map(str, starts))}" for enzyme, starts in find_sites(idt_dna).items()) or "none detected"
    return record, {
        "candidate_id": candidate_id,
        "idt_source_file": idt_source_file,
        "candidate_amino_acid_sequence": amino_acids,
        "codon_optimized_dna_sequence": idt_dna,
        "dna_length": str(len(idt_dna)),
        "dna_length_divisible_by_3": str(len(idt_dna) % 3 == 0),
        "translated_amino_acid_sequence": translate_dna(idt_dna),
        "translation_matches_intended_candidate": str(translate_dna(idt_dna) == amino_acids),
        "stop_codon_included": str(insert_expression.endswith(STOP_CODON)),
        "insert_in_frame_with_n_terminal_his_tag": str(full_translation == expected_full),
        "internal_restriction_sites": site_summary,
        "cloning_strategy_conflict": "none; seamless/Gibson strategy avoids dependence on internal restriction sites",
        "final_recommendation": "ready for vendor" if full_translation == expected_full and translate_dna(idt_dna) == amino_acids else "needs manual review",
        "expected_full_expressed_sequence": full_translation,
    }


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    GB_DIR.mkdir(parents=True, exist_ok=True)

    candidates = read_candidates()
    vector = snapgene_file_to_dict(str(VECTOR_DNA))["seq"].upper()

    order_rows: list[dict[str, str]] = []
    qc_rows: list[dict[str, str]] = []
    mapping_rows: list[dict[str, str]] = []

    for rank, candidate in enumerate(candidates, start=1):
        candidate_id = candidate["candidate_id"]
        path = idt_export_path(candidate_id)
        plasmid_name = f"pET28a-{candidate_id}"
        amino_acids = candidate["sequence"].strip().upper()
        idt_dna = read_idt_sequence(path)
        translated = translate_dna(idt_dna)
        if translated != amino_acids:
            raise ValueError(f"{path.name} translated as {translated}, expected {amino_acids} for {candidate_id}")

        source_path = f"plasmids/vendor_ready_pet28a_idt/idt_optimizer_exports/{path.name}"
        record, qc = make_record(plasmid_name, candidate_id, amino_acids, idt_dna, source_path, vector)
        SeqIO.write(record, GB_DIR / f"{plasmid_name}.gb", "genbank")

        mapping_rows.append(
            {
                "rank": str(rank),
                "candidate_id": candidate_id,
                "idt_source_file": source_path,
                "amino_acid_sequence": amino_acids,
                "idt_dna_sequence": idt_dna,
                "translated_sequence": translated,
                "translation_matches": str(translated == amino_acids),
            }
        )
        order_rows.append(
            {
                "candidate_id": candidate_id,
                "plasmid_name": plasmid_name,
                "amino_acid_sequence": amino_acids,
                "codon_optimized_dna_sequence": idt_dna,
                "cloning_strategy": "Seamless/Gibson cloning into pET-28a(+) after the BamHI-derived GS linker in the N-terminal His/T7 tag frame; replace downstream MCS sequence through XhoI region with IDT-optimized insert plus stop codon.",
                "vector": VECTOR,
                "antibiotic": ANTIBIOTIC,
                "promoter": PROMOTER,
                "tag_design": f"Preserve pET-28a(+) N-terminal {N_TERMINAL_LEADER} leader; add candidate sequence immediately after this leader; include stop codon before C-terminal vector-derived residues/tags.",
                "stop_codon_included": "yes (TAA)",
                "expected_expressed_protein_description": f"N-terminal His/T7 leader fused to {candidate_id}: {N_TERMINAL_LEADER}-{amino_acids}",
                "notes_for_vendor": f"Use IDT-optimized DNA from {source_path}. Synthesize candidate ORF with terminal TAA stop codon and clone in-frame downstream of the pET-28a(+) N-terminal His/T7 leader. Sequence-verify the full insert and both junctions.",
            }
        )
        qc_rows.append(qc)

    write_csv(OUTDIR / "idt_file_mapping.csv", mapping_rows)
    write_csv(OUTDIR / "plasmid_order_table.csv", order_rows)
    write_csv(OUTDIR / "plasmid_qc_report.csv", qc_rows)
    write_readme()
    write_qc_markdown(qc_rows)
    print(f"Wrote {len(order_rows)} IDT-based plasmid designs to {OUTDIR}")


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_readme() -> None:
    with (OUTDIR / "README_vendor_instructions.md").open("w") as handle:
        handle.write(
            "# pET-28a(+) LiSPER Vendor Instructions\n\n"
            "Please synthesize the listed codon-optimized inserts and clone each one into pET-28a(+) for E. coli BL21(DE3) expression. "
            "Preserve the N-terminal His-tag expression frame of pET-28a(+). Include a stop codon after each candidate coding sequence to avoid expression of unwanted C-terminal vector-derived residues/tags. "
            "Please sequence-verify the full insert and junction regions. Deliver plasmid DNA, final plasmid maps, full sequences, and Sanger sequencing reports.\n\n"
            "## Files\n\n"
            "- `idt_optimizer_exports/`: archived IDT codon optimizer exports and the optimization-order screenshot.\n"
            "- `idt_file_mapping.csv`: mapping from rank/candidate to the archived IDT export.\n"
            "- `plasmid_order_table.csv`: vendor order table with IDT-optimized insert sequences and design notes.\n"
            "- `plasmid_qc_report.csv`: per-construct translation, frame, stop-codon, and restriction-site QC.\n"
            "- `plasmid_qc_report.md`: compact human-readable QC summary.\n"
            "- `genbank/*.gb`: annotated circular GenBank plasmid maps for each construct.\n\n"
            "## Cloning Design\n\n"
            f"Use seamless/Gibson cloning into pET-28a(+) after the retained BamHI-derived `GS` linker in the N-terminal His/T7 expression frame. "
            f"The expected N-terminal vector-derived leader is `{N_TERMINAL_LEADER}`, followed immediately by the candidate sequence and a `{STOP_CODON}` stop codon.\n"
        )


def write_qc_markdown(qc_rows: list[dict[str, str]]) -> None:
    with (OUTDIR / "plasmid_qc_report.md").open("w") as handle:
        handle.write("# Plasmid QC Report\n\n")
        handle.write("| candidate_id | IDT source | dna_length | length_divisible_by_3 | translation_match | stop_codon | in_frame | internal_sites | recommendation |\n")
        handle.write("|---|---|---:|---|---|---|---|---|---|\n")
        for row in qc_rows:
            handle.write(
                f"| {row['candidate_id']} | {row['idt_source_file']} | {row['dna_length']} | {row['dna_length_divisible_by_3']} | "
                f"{row['translation_matches_intended_candidate']} | {row['stop_codon_included']} | "
                f"{row['insert_in_frame_with_n_terminal_his_tag']} | {row['internal_restriction_sites']} | {row['final_recommendation']} |\n"
            )


if __name__ == "__main__":
    main()
