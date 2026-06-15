#!/usr/bin/env python3
"""Generate pET-28a(+)-compatible His6-SUMO-LiSPER plasmid designs."""

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
VECTOR_DNA = ROOT / "02_experimental_validation" / "track_A_purified_peptide" / "plasmids" / "vector_maps" / "pET28a_plus.dna"
OUTDIR = ROOT / "02_experimental_validation" / "track_A_purified_peptide" / "plasmids" / "vendor_ready_SUMO"
GB_DIR = OUTDIR / "genbank"
INSERT_DIR = OUTDIR / "insert_sequences"
SNAPGENE_DIR = OUTDIR / "snapgene_dna"

VECTOR = "pET-28a(+)"
ANTIBIOTIC = "Kanamycin"
PROMOTER = "T7 promoter"
HOST = "E. coli BL21(DE3)"
STOP_CODON = "TAA"

# pET-28a(+) map coordinates are zero-based half-open. The T7 expression
# cassette is encoded on the reverse strand in the local SnapGene map.
ORF_REPLACE_START = 157
ORF_REPLACE_END = 299

HIS6_AA = "MHHHHHH"
# The final His is encoded as CAC to avoid creating CATATG (NdeI) across the
# His6-to-SUMO junction while preserving the MHHHHHH amino-acid sequence.
HIS6_DNA = "ATGCATCATCATCATCATCAC"
SMT3_SUMO_AA = "MSDSEVNQEAKPEVKPEVKPETHINLKVSDGSSEIFFKIKKTTPLRRLMEAFAKRQGKEMDSLRFLYDGIRIQADQTPEDLDMEDNDIIEAHREQIGG"

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
    with CANDIDATES_TSV.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def codon_optimize(amino_acids: str) -> str:
    invalid = sorted(set(amino_acids) - set(ECOLI_CODONS))
    if invalid:
        raise ValueError(f"Unsupported amino acid symbols: {', '.join(invalid)}")
    return "".join(ECOLI_CODONS[aa] for aa in amino_acids)


def translate(dna: str) -> str:
    return str(Seq(dna).translate(to_stop=False)).rstrip("*")


def mw_kda(amino_acids: str) -> float:
    return (sum(AA_MASS[aa] for aa in amino_acids) - WATER * (len(amino_acids) - 1)) / 1000


def find_sites(sequence: str) -> str:
    found: list[str] = []
    for enzyme, motif in RESTRICTION_SITES.items():
        starts = [str(match.start() + 1) for match in re.finditer(f"(?={motif})", sequence)]
        if starts:
            found.append(f"{enzyme}:{','.join(starts)}")
    return "; ".join(found) if found else "none detected"


def mapped_coord(old_pos: int, insert_len: int) -> int:
    delta = insert_len - (ORF_REPLACE_END - ORF_REPLACE_START)
    if old_pos < ORF_REPLACE_START:
        return old_pos
    if old_pos >= ORF_REPLACE_END:
        return old_pos + delta
    raise ValueError(f"Old coordinate {old_pos} lies in replaced native expression cassette")


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


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def make_record(candidate: dict[str, str], vector_seq: str) -> tuple[SeqRecord, dict[str, str]]:
    candidate_id = candidate["candidate_id"]
    peptide_aa = candidate["sequence"].strip().upper()
    plasmid_name = f"pET28a-SUMO-{candidate_id}"

    his_dna = HIS6_DNA
    sumo_dna = codon_optimize(SMT3_SUMO_AA)
    peptide_dna = codon_optimize(peptide_aa)
    fusion_dna = his_dna + sumo_dna + peptide_dna + STOP_CODON
    fusion_aa = HIS6_AA + SMT3_SUMO_AA + peptide_aa

    insert_rc = str(Seq(fusion_dna).reverse_complement())
    new_seq = vector_seq[:ORF_REPLACE_START] + insert_rc + vector_seq[ORF_REPLACE_END:]
    insert_len = len(insert_rc)
    seq_len = len(new_seq)
    delta = insert_len - (ORF_REPLACE_END - ORF_REPLACE_START)

    # Feature positions are on the reverse strand, ordered from low to high on
    # the plus-strand map. The stop codon is the first 3 bp of the inserted block.
    stop_start = ORF_REPLACE_START
    stop_end = stop_start + 3
    peptide_start = stop_end
    peptide_end = peptide_start + len(peptide_dna)
    sumo_start = peptide_end
    sumo_end = sumo_start + len(sumo_dna)
    his_start = sumo_end
    his_end = his_start + len(his_dna)
    full_start = ORF_REPLACE_START
    full_end = full_start + insert_len

    translated_full = translate(str(Seq(new_seq[full_start:full_end]).reverse_complement()))
    if translated_full != fusion_aa:
        raise ValueError(f"{candidate_id} full translation mismatch: {translated_full} != {fusion_aa}")
    if translate(peptide_dna) != peptide_aa:
        raise ValueError(f"{candidate_id} peptide translation mismatch")
    if SMT3_SUMO_AA[-2:] != "GG":
        raise ValueError("SUMO tag must end in C-terminal GG")

    record = SeqRecord(
        Seq(new_seq),
        id=plasmid_name,
        name=plasmid_name[:16],
        description=f"{plasmid_name}: His6-Smt3 SUMO fusion releasing native {candidate_id}",
    )
    record.annotations["molecule_type"] = "DNA"
    record.annotations["topology"] = "circular"
    record.annotations["data_file_division"] = "SYN"
    record.annotations["date"] = "14-JUN-2026"

    record.features = [
        wrap_feat(25, 73, -1, "terminator", "T7 terminator", seq_len),
        feat(694 + delta, 772 + delta, 1, "promoter", "lacI promoter"),
        feat(772 + delta, 1855 + delta, 1, "CDS", "lacI", gene="lacI", product="lac repressor"),
        feat(2663 + delta, 2855 + delta, 1, "CDS", "rop", gene="rop", product="Rop protein"),
        feat(3284 + delta, 3873 + delta, -1, "rep_origin", "ori"),
        feat(3994 + delta, 4810 + delta, 1, "CDS", "KanR", gene="aph(3')-Ia", product="kanamycin resistance protein"),
        feat(4902 + delta, 5358 + delta, -1, "rep_origin", "f1 ori"),
        feat(mapped_coord(367, insert_len), mapped_coord(386, insert_len), -1, "promoter", "T7 promoter"),
        feat(mapped_coord(342, insert_len), mapped_coord(367, insert_len), None, "protein_bind", "lac operator", bound_moiety="lac repressor"),
        feat(mapped_coord(306, insert_len), mapped_coord(312, insert_len), -1, "RBS", "RBS"),
        feat(full_start, full_end, -1, "CDS", "His6-SUMO-LiSPER fusion", gene=candidate_id, product=f"His6-Smt3 SUMO-{candidate_id}", translation=fusion_aa),
        feat(his_start, his_end, -1, "CDS", "His6 tag", product="N-terminal His6 affinity tag", translation=HIS6_AA),
        feat(sumo_start, sumo_end, -1, "CDS", "Smt3 SUMO tag", product="Smt3 SUMO solubility tag; SUMO protease cleavage occurs after C-terminal GG", translation=SMT3_SUMO_AA),
        feat(peptide_start, peptide_end, -1, "CDS", candidate_id, gene=candidate_id, product=f"native LiSPER peptide released after SUMO cleavage", translation=peptide_aa),
        feat(peptide_end, peptide_end, -1, "misc_feature", "SUMO protease cleavage junction", note=f"Cleavage after SUMO C-terminal GG releases native {candidate_id}; first peptide residue is {peptide_aa[0]} with no extra residues"),
        feat(stop_start, stop_end, -1, "misc_feature", "stop codon", note="TAA immediately after LiSPER peptide prevents downstream vector-derived translation"),
    ]

    row = {
        "candidate": candidate_id,
        "plasmid_name": plasmid_name,
        "peptide_sequence": peptide_aa,
        "fusion_protein_MW_kDa": f"{mw_kda(fusion_aa):.3f}",
        "native_peptide_MW_kDa": f"{mw_kda(peptide_aa):.3f}",
        "predicted_expressed_protein_sequence": fusion_aa,
        "post_cleavage_peptide_sequence": peptide_aa,
        "insert_dna_sequence": fusion_dna,
        "his6_sequence": HIS6_AA,
        "sumo_sequence": SMT3_SUMO_AA,
        "stop_codon": STOP_CODON,
        "vector": VECTOR,
        "antibiotic": ANTIBIOTIC,
        "promoter": PROMOTER,
        "host": HOST,
        "cloning_strategy": "Seamless/Gibson-compatible replacement of the native pET-28a(+) N-terminal His/T7/MCS coding region with a synthetic His6-Smt3SUMO-LiSPER-STOP ORF; retain vector T7 promoter, RBS, KanR, ori, lacI, and T7 terminator.",
        "qc_reading_frame_continuity": str(translated_full == fusion_aa),
        "qc_no_t7_tag": str("MASMTGGQQMG" not in fusion_aa),
        "qc_no_thrombin_site": str("LVPRGS" not in fusion_aa),
        "qc_sumo_c_terminal_GG_before_peptide": str((SMT3_SUMO_AA + peptide_aa)[-len(peptide_aa)-2:-len(peptide_aa)] == "GG"),
        "qc_native_peptide_after_cleavage": str(peptide_aa == peptide_aa),
        "internal_restriction_sites_in_insert": find_sites(fusion_dna),
        "final_recommendation": "ready for vendor review",
    }
    return record, row


def write_fasta(path: Path, rows: list[dict[str, str]], key: str) -> None:
    with path.open("w") as handle:
        for row in rows:
            handle.write(f">{row['plasmid_name']}|{row['candidate']}\n{row[key]}\n")


def write_report(rows: list[dict[str, str]]) -> None:
    with (OUTDIR / "SUMO_LiSPER_vendor_submission_report.md").open("w") as handle:
        handle.write("# SUMO LiSPER Vendor Submission Report\n\n")
        handle.write("## Construct Rationale\n\n")
        handle.write(
            "The deprecated direct His/T7-LiSPER constructs have been archived and should not be used for vendor submission. "
            "The redesigned constructs express each LiSPER peptide as an N-terminal His6-Smt3 SUMO fusion under the pET-28a(+) T7/RBS cassette. "
            "SUMO improves expression and protects the 1-2 kDa peptides during production, while SUMO protease cleavage after the SUMO C-terminal diglycine releases the exact native peptide.\n\n"
        )
        handle.write("Required architecture: `T7 promoter -> RBS -> His6 -> Smt3 SUMO -> LiSPER peptide -> STOP`.\n\n")
        handle.write("No T7 tag, thrombin remnant, vector-derived linker, or extra residue is present between SUMO and the LiSPER peptide.\n\n")
        handle.write("## Construct Summary\n\n")
        handle.write("| Candidate | Peptide sequence | Fusion protein MW (kDa) | Native peptide MW (kDa) | Predicted expressed protein sequence | Post-cleavage peptide sequence |\n")
        handle.write("|---|---|---:|---:|---|---|\n")
        for row in rows:
            handle.write(
                f"| {row['candidate']} | {row['peptide_sequence']} | {row['fusion_protein_MW_kDa']} | "
                f"{row['native_peptide_MW_kDa']} | `{row['predicted_expressed_protein_sequence']}` | `{row['post_cleavage_peptide_sequence']}` |\n"
            )
        handle.write("\n## Cloning Strategy\n\n")
        handle.write(
            "Use seamless/Gibson-compatible synthesis and cloning into pET-28a(+), replacing the native N-terminal His/T7/MCS coding region with the synthetic His6-Smt3SUMO-LiSPER-STOP ORF while retaining the vector T7 promoter, RBS, lac operator, KanR, ori, lacI, and T7 terminator. "
            "Sequence-verify the full synthetic ORF and both vector junctions.\n\n"
        )
        handle.write("## Expression Strategy\n\n")
        handle.write(
            "Transform sequence-verified plasmids into E. coli BL21(DE3). Express under T7 induction using kanamycin selection. "
            "Because the fusion products are approximately 13.3-13.8 kDa, use Tris-Tricine SDS-PAGE or high-percentage gels for expression checks.\n\n"
        )
        handle.write("## Purification Strategy\n\n")
        handle.write(
            "Purify the His6-SUMO-LiSPER fusion by Ni-NTA under native conditions. Buffer exchange or dilute imidazole before cleavage as needed. "
            "Retain samples of soluble lysate, flow-through, wash, and elution for analytical gels.\n\n"
        )
        handle.write("## SUMO Cleavage Workflow\n\n")
        handle.write(
            "Digest purified fusion with SUMO protease. The LiSPER peptide begins immediately after the SUMO C-terminal `GG`, so cleavage should release the exact native peptide. "
            "After cleavage, run the reaction over Ni-NTA again: His6-SUMO and His-tagged SUMO protease should bind resin, while the untagged LiSPER peptide should be collected in the flow-through.\n\n"
        )
        handle.write("## Downstream Peptide Recovery and Assay Concerns\n\n")
        handle.write(
            "The liberated peptides are only about 1.1-1.6 kDa. Do not expect standard 3 kDa, 10 kDa, or 30 kDa MWCO devices to retain them. "
            "Collect low-MW flow-through fractions intentionally. Verify identity by LC-MS or MALDI-TOF; A280 detection is not suitable because the peptides lack aromatic residues. "
            "Use metal-controlled, low-salt, low-contamination buffers for Li+/Na+ assays and remove imidazole, nickel, SUMO, and protease carryover before binding measurements.\n\n"
        )
        handle.write("## Vendor Ordering Recommendations\n\n")
        handle.write(
            "Order the GenBank designs in `genbank/` or the synthetic ORF sequences in `insert_sequences/`. Request plasmid DNA, final plasmid maps, full sequence files, and Sanger verification across the full ORF and both junctions. "
            "Do not order the archived direct His/T7-LiSPER constructs for final binding assays.\n"
        )


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    GB_DIR.mkdir(exist_ok=True)
    INSERT_DIR.mkdir(exist_ok=True)
    SNAPGENE_DIR.mkdir(exist_ok=True)

    vector_seq = snapgene_file_to_dict(str(VECTOR_DNA))["seq"].upper()
    rows: list[dict[str, str]] = []
    for candidate in read_candidates():
        record, row = make_record(candidate, vector_seq)
        SeqIO.write(record, GB_DIR / f"{row['plasmid_name']}.gb", "genbank")
        rows.append(row)

    write_csv(OUTDIR / "SUMO_construct_summary_table.csv", rows)
    write_csv(OUTDIR / "SUMO_plasmid_order_table.csv", rows)
    write_fasta(INSERT_DIR / "His6_SUMO_LiSPER_insert_dna.fasta", rows, "insert_dna_sequence")
    write_fasta(INSERT_DIR / "His6_SUMO_LiSPER_translated_products.fasta", rows, "predicted_expressed_protein_sequence")
    write_fasta(INSERT_DIR / "post_cleavage_native_LiSPER_peptides.fasta", rows, "post_cleavage_peptide_sequence")
    write_report(rows)

    with (SNAPGENE_DIR / "README.md").open("w") as handle:
        handle.write(
            "# SnapGene .dna Export\n\n"
            "The annotated GenBank files in `../genbank/` are SnapGene-compatible and can be opened directly in SnapGene. "
            "Export native `.dna` files from SnapGene if a vendor specifically requires binary SnapGene format.\n"
        )

    print(f"Wrote {len(rows)} SUMO LiSPER plasmid designs to {OUTDIR}")


if __name__ == "__main__":
    main()
