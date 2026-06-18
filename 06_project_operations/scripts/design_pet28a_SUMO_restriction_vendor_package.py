#!/usr/bin/env python3
"""Generate vendor-friendly pET-28a(+)/NdeI-XhoI His6-SUMO-LiSPER designs.

This package deliberately treats pET-28a(+) as a real vendor backbone:
the vendor synthesizes only the insert and restriction-clones it into the
original pET-28a(+) MCS. The final GenBank maps are target constructs for
review/verification, not requests to synthesize an entire altered vector.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import CompoundLocation, FeatureLocation, SeqFeature
from Bio.SeqRecord import SeqRecord
from snapgene_reader import snapgene_file_to_dict


ROOT = Path(__file__).resolve().parents[2]
CANDIDATES_TSV = ROOT / "01_computational_discovery" / "sequences" / "candidates.tsv"
PLASMID_DIR = ROOT / "02_experimental_validation" / "track_A_purified_peptide" / "plasmids"
VECTOR_DNA = PLASMID_DIR / "vector_maps" / "pET28a_plus.dna"
IDT_CODON_MANIFEST = PLASMID_DIR / "codon_optimization" / "idt_peptide_codon_optimization.csv"
OUTDIR = PLASMID_DIR / "vendor_ready_restriction_SUMO"
GB_DIR = OUTDIR / "genbank_final_constructs"
INSERT_DIR = OUTDIR / "insert_sequences"

VECTOR = "pET-28a(+)"
ANTIBIOTIC = "Kanamycin"
HOST = "E. coli BL21(DE3)"
STOP_CODON = "TAA"

# Coordinates in the local pET-28a(+) SnapGene file, zero-based half-open.
# The expression cassette is on the reverse strand in this map. The corrected
# vendor design replaces only the NdeI/XhoI restriction-cloning fragment.
XHOI_START = 157
XHOI_END = 163
NDEI_START = 236
NDEI_END = 242
REPLACE_START = XHOI_START
REPLACE_END = NDEI_END

NDEI = "CATATG"
XHOI = "CTCGAG"

HIS6_AA = "MHHHHHH"
HIS6_DNA = "ATGCATCATCATCATCATCAC"
SMT3_SUMO_AA = (
    "MSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGK"
    "EMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGG"
)

ECOLI_CODONS = {
    "A": "GCG",
    "C": "TGC",
    "D": "GAT",
    "E": "GAA",
    "F": "TTT",
    "G": "GGT",
    "H": "CAT",
    "I": "ATT",
    "K": "AAA",
    "L": "CTG",
    "M": "ATG",
    "N": "AAT",
    "P": "CCG",
    "Q": "CAG",
    "R": "CGT",
    "S": "TCT",
    "T": "ACC",
    "V": "GTG",
    "W": "TGG",
    "Y": "TAT",
}

AA_MASS = {
    "A": 89.09,
    "R": 174.20,
    "N": 132.12,
    "D": 133.10,
    "C": 121.16,
    "E": 147.13,
    "Q": 146.15,
    "G": 75.07,
    "H": 155.16,
    "I": 131.17,
    "L": 131.17,
    "K": 146.19,
    "M": 149.21,
    "F": 165.19,
    "P": 115.13,
    "S": 105.09,
    "T": 119.12,
    "W": 204.23,
    "Y": 181.19,
    "V": 117.15,
}
WATER = 18.01528

RESTRICTION_SITES = {
    "NdeI": NDEI,
    "XhoI": XHOI,
    "NcoI": "CCATGG",
    "BamHI": "GGATCC",
    "EcoRI": "GAATTC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "SacI": "GAGCTC",
    "SalI": "GTCGAC",
}


def read_candidates() -> list[dict[str, str]]:
    with CANDIDATES_TSV.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def read_idt_peptide_codons() -> dict[str, dict[str, str]]:
    """Read IDT-optimized peptide coding sequences keyed by candidate id."""
    if not IDT_CODON_MANIFEST.exists():
        raise FileNotFoundError(
            f"Missing IDT peptide codon manifest: {IDT_CODON_MANIFEST}. "
            "Download/process IDT codon optimization before generating vendor plasmids."
        )
    with IDT_CODON_MANIFEST.open(newline="") as handle:
        return {row["candidate_id"]: row for row in csv.DictReader(handle)}


def codon_optimize(amino_acids: str) -> str:
    invalid = sorted(set(amino_acids) - set(ECOLI_CODONS))
    if invalid:
        raise ValueError(f"Unsupported amino acid symbols: {', '.join(invalid)}")
    return "".join(ECOLI_CODONS[aa] for aa in amino_acids)


def translate(dna: str) -> str:
    return str(Seq(dna).translate(to_stop=False)).rstrip("*")


def mw_kda(amino_acids: str) -> float:
    return (sum(AA_MASS[aa] for aa in amino_acids) - WATER * (len(amino_acids) - 1)) / 1000


def sites_in(sequence: str, site_names: tuple[str, ...]) -> str:
    hits: list[str] = []
    for name in site_names:
        motif = RESTRICTION_SITES[name]
        starts = [str(match.start() + 1) for match in re.finditer(f"(?={motif})", sequence)]
        if starts:
            hits.append(f"{name}:{','.join(starts)}")
    return "; ".join(hits) if hits else "none detected"


def feat(start: int, end: int, strand: int | None, ftype: str, label: str, **quals) -> SeqFeature:
    qualifiers = {"label": label}
    qualifiers.update({key: value for key, value in quals.items() if value is not None})
    return SeqFeature(FeatureLocation(start, end, strand=strand), type=ftype, qualifiers=qualifiers)


def wrap_feat(start: int, end: int, strand: int | None, ftype: str, label: str, seq_len: int, **quals) -> SeqFeature:
    qualifiers = {"label": label}
    qualifiers.update({key: value for key, value in quals.items() if value is not None})
    if start <= end:
        loc = FeatureLocation(start, end, strand=strand)
    else:
        loc = CompoundLocation([FeatureLocation(start, seq_len, strand=strand), FeatureLocation(0, end, strand=strand)])
    return SeqFeature(loc, type=ftype, qualifiers=qualifiers)


def shifted(old_pos: int, delta: int) -> int:
    if old_pos <= REPLACE_START:
        return old_pos
    if old_pos >= REPLACE_END:
        return old_pos + delta
    raise ValueError(f"Coordinate {old_pos} lies inside the NdeI/XhoI replacement interval")


def make_record(
    candidate: dict[str, str],
    peptide_codons: dict[str, dict[str, str]],
    vector_seq: str,
) -> tuple[SeqRecord, dict[str, str]]:
    candidate_id = candidate["candidate_id"]
    peptide_aa = candidate["sequence"].strip().upper()
    plasmid_name = f"pET28a-SUMO-{candidate_id}"
    if candidate_id not in peptide_codons:
        raise ValueError(f"{candidate_id}: missing IDT peptide codon optimization row")

    sumo_dna = codon_optimize(SMT3_SUMO_AA)
    peptide_dna = peptide_codons[candidate_id]["idt_optimized_dna"].strip().upper()
    if translate(peptide_dna) != peptide_aa:
        raise ValueError(
            f"{candidate_id}: IDT peptide codons translate to {translate(peptide_dna)}, "
            f"expected {peptide_aa}"
        )
    orf_dna = HIS6_DNA + sumo_dna + peptide_dna + STOP_CODON
    orf_aa = HIS6_AA + SMT3_SUMO_AA + peptide_aa

    if not orf_dna.startswith("ATG"):
        raise ValueError(f"{candidate_id}: ORF does not start with ATG")
    if translate(orf_dna) != orf_aa:
        raise ValueError(f"{candidate_id}: ORF translation mismatch")

    # NdeI contains the ATG start codon. Do not duplicate ATG after NdeI.
    insert_coding = NDEI + orf_dna[3:] + XHOI
    replacement_plus = str(Seq(insert_coding).reverse_complement())
    final_seq = vector_seq[:REPLACE_START] + replacement_plus + vector_seq[REPLACE_END:]
    delta = len(replacement_plus) - (REPLACE_END - REPLACE_START)
    seq_len = len(final_seq)
    rel_len = len(replacement_plus)

    if final_seq[REPLACE_START:REPLACE_START + 6] != XHOI:
        raise ValueError(f"{candidate_id}: XhoI boundary not preserved in final map")
    if final_seq[REPLACE_START + rel_len - 6:REPLACE_START + rel_len] != NDEI:
        raise ValueError(f"{candidate_id}: NdeI boundary not preserved in final map")

    def coding_loc(start: int, end: int) -> tuple[int, int]:
        """Map final-insert coding-strand coordinates to plus-strand map coordinates."""
        return REPLACE_START + rel_len - end, REPLACE_START + rel_len - start

    orf_start, orf_end = coding_loc(3, 3 + len(orf_dna))
    his_start, his_end = coding_loc(3, 3 + len(HIS6_DNA))
    sumo_start, sumo_end = coding_loc(3 + len(HIS6_DNA), 3 + len(HIS6_DNA) + len(sumo_dna))
    peptide_start, peptide_end = coding_loc(
        3 + len(HIS6_DNA) + len(sumo_dna),
        3 + len(HIS6_DNA) + len(sumo_dna) + len(peptide_dna),
    )
    stop_start, stop_end = coding_loc(3 + len(orf_dna) - 3, 3 + len(orf_dna))

    translated_final = translate(str(Seq(final_seq[orf_start:orf_end]).reverse_complement()))
    if translated_final != orf_aa:
        raise ValueError(f"{candidate_id}: final plasmid CDS translation mismatch")

    record = SeqRecord(
        Seq(final_seq),
        id=plasmid_name,
        name=plasmid_name[:16],
        description=f"{plasmid_name}: pET-28a(+) NdeI/XhoI His6-SUMO-{candidate_id}",
    )
    record.annotations["molecule_type"] = "DNA"
    record.annotations["topology"] = "circular"
    record.annotations["data_file_division"] = "SYN"
    record.annotations["date"] = "18-JUN-2026"

    record.features = [
        wrap_feat(25, 73, -1, "terminator", "T7 terminator", seq_len),
        feat(shifted(694, delta), shifted(772, delta), 1, "promoter", "lacI promoter"),
        feat(shifted(772, delta), shifted(1855, delta), 1, "CDS", "lacI", gene="lacI", product="lac repressor"),
        feat(shifted(2663, delta), shifted(2855, delta), 1, "CDS", "rop", gene="rop", product="Rop protein"),
        feat(shifted(3284, delta), shifted(3873, delta), -1, "rep_origin", "ori"),
        feat(shifted(3994, delta), shifted(4810, delta), 1, "CDS", "KanR", gene="aph(3')-Ia", product="kanamycin resistance protein"),
        feat(shifted(4902, delta), shifted(5358, delta), -1, "rep_origin", "f1 ori"),
        feat(shifted(367, delta), shifted(386, delta), -1, "promoter", "T7 promoter"),
        feat(shifted(342, delta), shifted(367, delta), None, "protein_bind", "lac operator", bound_moiety="lac repressor"),
        feat(shifted(306, delta), shifted(312, delta), -1, "RBS", "RBS"),
        feat(REPLACE_START, REPLACE_START + 6, None, "misc_feature", "XhoI cloning site", note="3' cloning boundary downstream of stop codon"),
        feat(REPLACE_START + rel_len - 6, REPLACE_START + rel_len, None, "misc_feature", "NdeI cloning site", note="5' cloning boundary; ATG start codon is inside NdeI"),
        feat(REPLACE_START, REPLACE_START + rel_len, -1, "misc_feature", "vendor cloned insert", note="Synthesized insert cloned into original pET-28a(+) using NdeI/XhoI"),
        feat(orf_start, orf_end, -1, "CDS", "His6-SUMO-LiSPER fusion", gene=candidate_id, product=f"His6-Smt3 SUMO-{candidate_id}", translation=orf_aa),
        feat(his_start, his_end, -1, "CDS", "His6 tag", product="N-terminal His6 affinity tag", translation=HIS6_AA),
        feat(sumo_start, sumo_end, -1, "CDS", "Smt3 SUMO tag", product="Smt3 SUMO solubility tag", translation=SMT3_SUMO_AA),
        feat(peptide_start, peptide_end, -1, "CDS", candidate_id, gene=candidate_id, product="native LiSPER peptide released after SUMO cleavage", translation=peptide_aa),
        feat(peptide_end, peptide_end, -1, "misc_feature", "SUMO protease cleavage junction", note="Cleavage after SUMO C-terminal GG releases native LiSPER peptide with no extra residues"),
        feat(stop_start, stop_end, -1, "misc_feature", "TAA stop codon", note="Stop codon precedes XhoI to prevent vector-derived C-terminal residues"),
    ]

    internal_sites = sites_in(orf_dna, ("NdeI", "XhoI"))
    row = {
        "candidate_id": candidate_id,
        "plasmid_name": plasmid_name,
        "backbone": VECTOR,
        "host_for_expression": HOST,
        "antibiotic": ANTIBIOTIC,
        "peptide_sequence": peptide_aa,
        "fusion_protein_sequence": orf_aa,
        "post_SUMO_cleavage_peptide": peptide_aa,
        "fusion_MW_kDa": f"{mw_kda(orf_aa):.3f}",
        "native_peptide_MW_kDa": f"{mw_kda(peptide_aa):.3f}",
        "idt_peptide_codon_source": peptide_codons[candidate_id]["source_file"],
        "idt_peptide_coding_sequence": peptide_dna,
        "complete_ORF_without_restriction_sites": orf_dna,
        "synthesis_insert_NdeI_to_XhoI": insert_coding,
        "insert_length_bp": str(len(insert_coding)),
        "final_plasmid_length_bp": str(len(final_seq)),
        "internal_NdeI_XhoI_check": "PASS: no internal NdeI/XhoI in ORF" if internal_sites == "none detected" else f"FAIL: {internal_sites}",
        "boundary_check": "PASS: final construct preserves NdeI and XhoI cloning boundaries",
        "translation_check": "PASS",
        "vendor_action": "Synthesize insert only; clone into original pET-28a(+) backbone using NdeI/XhoI; sequence verify insert and both junctions.",
    }
    return record, row


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_fasta(path: Path, rows: list[dict[str, str]], key: str) -> None:
    with path.open("w") as handle:
        for row in rows:
            handle.write(f">{row['plasmid_name']}|{row['candidate_id']}\n{row[key]}\n")


def write_vendor_instructions(rows: list[dict[str, str]]) -> None:
    with (OUTDIR / "VENDOR_ORDER_INSTRUCTIONS.md").open("w") as handle:
        handle.write("# Vendor Order Instructions: pET-28a(+)-His6-SUMO-LiSPER Inserts\n\n")
        handle.write("## Critical Clarification\n\n")
        handle.write(
            "Please **do not synthesize a redesigned full pET-28a plasmid**. "
            "Please use a standard/original pET-28a(+) backbone and synthesize only the listed inserts. "
            "Each insert should be restriction-cloned into the original pET-28a(+) MCS using **NdeI and XhoI**.\n\n"
        )
        handle.write("## Cloning Strategy\n\n")
        handle.write("- Backbone: original pET-28a(+), kanamycin resistance.\n")
        handle.write("- Expression host after delivery: E. coli BL21(DE3).\n")
        handle.write("- 5' cloning site: NdeI (`CATATG`). The ATG start codon is inside the NdeI site.\n")
        handle.write("- 3' cloning site: XhoI (`CTCGAG`) downstream of a TAA stop codon.\n")
        handle.write("- Insert architecture: `NdeI -> His6 -> Smt3 SUMO -> LiSPER peptide -> TAA stop -> XhoI`.\n")
        handle.write("- LiSPER peptide-coding segments use the IDT E. coli codon-optimized sequences in `codon_optimization/idt_peptide_codon_optimization.csv`.\n")
        handle.write("- Important: do not duplicate the ATG after NdeI. Use the exact insert sequences in the order table.\n")
        handle.write("- Please sequence-verify the complete insert and both vector-insert junctions.\n\n")
        handle.write("## Why This Fixes the Previous Problem\n\n")
        handle.write(
            "The previous style of design changed too much of the pET-28a MCS/expression region and did not match a normal insert-into-backbone vendor workflow. "
            "This package instead keeps the vector as pET-28a(+) and defines only a restriction-cloned insert between the existing NdeI and XhoI sites.\n\n"
        )
        handle.write("## Construct Summary\n\n")
        handle.write("| Candidate | Plasmid | Peptide | Insert length (bp) | QC |\n")
        handle.write("|---|---|---|---:|---|\n")
        for row in rows:
            handle.write(
                f"| {row['candidate_id']} | {row['plasmid_name']} | `{row['peptide_sequence']}` | "
                f"{row['insert_length_bp']} | {row['internal_NdeI_XhoI_check']}; {row['translation_check']} |\n"
            )
        handle.write("\n## Files\n\n")
        handle.write("- `vendor_order_table.csv`: insert sequences and construct QC.\n")
        handle.write("- `insert_sequences/`: FASTA files for synthesis inserts, translated fusion products, and post-cleavage peptides.\n")
        handle.write("- `genbank_final_constructs/`: target final plasmid maps for review and sequence verification.\n\n")
        handle.write("## Protein Product\n\n")
        handle.write(
            "Each construct expresses an N-terminal His6-Smt3 SUMO fusion. SUMO protease cleavage after the SUMO C-terminal `GG` should release the native LiSPER peptide exactly, with no extra N-terminal or C-terminal residues.\n"
        )


def write_readme(rows: list[dict[str, str]]) -> None:
    with (OUTDIR / "README.md").open("w") as handle:
        handle.write("# Vendor-Ready Restriction-Cloning SUMO Plasmids\n\n")
        handle.write(
            "This folder contains the corrected purified-peptide plasmid vendor package for the final 8 LiSPER candidates. "
            "The package follows the vendor-compatible rule: synthesize only the insert, then clone it into an original pET-28a(+) backbone by NdeI/XhoI restriction cloning.\n\n"
        )
        handle.write(
            "The LiSPER peptide-coding regions use the IDT E. coli codon-optimized sequences stored in "
            "`../codon_optimization/idt_peptide_codon_optimization.csv`.\n\n"
        )
        handle.write("## Folder Contents\n\n")
        handle.write("| Path | Purpose |\n|---|---|\n")
        handle.write("| `VENDOR_ORDER_INSTRUCTIONS.md` | Human-readable instructions to send/review with the vendor. |\n")
        handle.write("| `vendor_order_table.csv` | Complete insert sequences and QC fields. |\n")
        handle.write("| `genbank_final_constructs/` | Eight target final plasmid GenBank maps. |\n")
        handle.write("| `insert_sequences/` | FASTA files for synthesis inserts and translated products. |\n\n")
        handle.write("## Constructs\n\n")
        handle.write("| Candidate | Plasmid | Product |\n|---|---|---|\n")
        for row in rows:
            handle.write(f"| `{row['candidate_id']}` | `{row['plasmid_name']}` | His6-SUMO-`{row['candidate_id']}` |\n")


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    GB_DIR.mkdir(exist_ok=True)
    INSERT_DIR.mkdir(exist_ok=True)

    vector_seq = snapgene_file_to_dict(str(VECTOR_DNA))["seq"].upper()
    if vector_seq[XHOI_START:XHOI_END] != XHOI or vector_seq[NDEI_START:NDEI_END] != NDEI:
        raise ValueError("The local pET-28a(+) map does not match expected NdeI/XhoI coordinates")

    peptide_codons = read_idt_peptide_codons()
    rows: list[dict[str, str]] = []
    for candidate in read_candidates():
        record, row = make_record(candidate, peptide_codons, vector_seq)
        SeqIO.write(record, GB_DIR / f"{row['plasmid_name']}.gb", "genbank")
        rows.append(row)

    write_csv(OUTDIR / "vendor_order_table.csv", rows)
    write_fasta(INSERT_DIR / "NdeI_XhoI_synthesis_inserts.fasta", rows, "synthesis_insert_NdeI_to_XhoI")
    write_fasta(INSERT_DIR / "His6_SUMO_LiSPER_ORFs_without_restriction_sites.fasta", rows, "complete_ORF_without_restriction_sites")
    write_fasta(INSERT_DIR / "His6_SUMO_LiSPER_fusion_proteins.fasta", rows, "fusion_protein_sequence")
    write_fasta(INSERT_DIR / "post_SUMO_cleavage_native_peptides.fasta", rows, "post_SUMO_cleavage_peptide")
    write_vendor_instructions(rows)
    write_readme(rows)
    print(f"Wrote {len(rows)} corrected vendor-ready plasmid designs to {OUTDIR}")


if __name__ == "__main__":
    main()
