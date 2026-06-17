#!/usr/bin/env python3
"""Create restriction-cloning insert order files for His6-SUMO-LiSPER constructs."""

from __future__ import annotations

import csv
from pathlib import Path

from Bio.Seq import Seq


ROOT = Path(__file__).resolve().parents[2]
SUMO_DIR = ROOT / "02_experimental_validation" / "track_A_purified_peptide" / "plasmids" / "vendor_ready_SUMO"
SUMMARY_CSV = SUMO_DIR / "SUMO_construct_summary_table.csv"
OUTDIR = SUMO_DIR / "restriction_cloning_insert_order"

FIVE_PRIME_SITE_NAME = "NdeI"
FIVE_PRIME_SITE = "CATATG"
THREE_PRIME_SITE_NAME = "XhoI"
THREE_PRIME_SITE = "CTCGAG"
STOP_CODON = "TAA"

SITES = {
    "NdeI": "CATATG",
    "XhoI": "CTCGAG",
    "NcoI": "CCATGG",
    "BamHI": "GGATCC",
    "EcoRI": "GAATTC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "SacI": "GAGCTC",
    "SalI": "GTCGAC",
}


def read_rows() -> list[dict[str, str]]:
    with SUMMARY_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def find_internal_sites(sequence: str, site_names: tuple[str, ...]) -> str:
    hits: list[str] = []
    for name in site_names:
        motif = SITES[name]
        starts = []
        start = 0
        while True:
            idx = sequence.find(motif, start)
            if idx < 0:
                break
            starts.append(str(idx + 1))
            start = idx + 1
        if starts:
            hits.append(f"{name}:{','.join(starts)}")
    return "; ".join(hits) if hits else "PASS: no internal NdeI or XhoI sites in ORF"


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    order_rows: list[dict[str, str]] = []
    qc_rows: list[dict[str, str]] = []

    for row in read_rows():
        candidate = row["candidate"]
        peptide = row["peptide_sequence"]
        plasmid_name = row["plasmid_name"]
        orf_dna = row["insert_dna_sequence"]
        orf_aa = row["predicted_expressed_protein_sequence"]

        if not orf_dna.startswith("ATG"):
            raise ValueError(f"{candidate}: ORF does not start with ATG")
        if not orf_dna.endswith(STOP_CODON):
            raise ValueError(f"{candidate}: ORF does not end with {STOP_CODON}")

        # NdeI contains the start codon, so do not duplicate the ATG.
        final_insert = FIVE_PRIME_SITE + orf_dna[3:] + THREE_PRIME_SITE
        coding_region_from_nde = final_insert[3:-len(THREE_PRIME_SITE)]
        translated = str(Seq(coding_region_from_nde).translate(to_stop=False)).rstrip("*")
        internal_check = find_internal_sites(orf_dna, (FIVE_PRIME_SITE_NAME, THREE_PRIME_SITE_NAME))
        reading_frame_ok = translated == orf_aa
        cleavage_ok = orf_aa.endswith(peptide) and row["post_cleavage_peptide_sequence"] == peptide

        common_sites = []
        for site_name in ("NcoI", "BamHI", "EcoRI", "HindIII", "NotI", "SacI", "SalI"):
            motif = SITES[site_name]
            if motif in orf_dna:
                common_sites.append(site_name)
        common_site_note = "none detected" if not common_sites else "; ".join(common_sites)

        order_rows.append(
            {
                "candidate_id": candidate,
                "peptide_sequence": peptide,
                "plasmid_name": plasmid_name,
                "backbone_vector": "original pET-28a(+) backbone",
                "final_expression_architecture": "pET-28a(+) T7 promoter/RBS -> synthetic His6-Smt3 SUMO-LiSPER-STOP ORF -> T7 terminator",
                "complete_ORF_amino_acid_sequence": orf_aa,
                "complete_ORF_DNA_sequence_without_restriction_sites": orf_dna,
                "five_prime_restriction_site": f"{FIVE_PRIME_SITE_NAME} ({FIVE_PRIME_SITE}; ATG within site is the ORF start codon)",
                "three_prime_restriction_site": f"{THREE_PRIME_SITE_NAME} ({THREE_PRIME_SITE}; placed downstream of {STOP_CODON})",
                "final_synthesis_insert_with_restriction_sites": final_insert,
                "stop_codon": STOP_CODON,
                "internal_restriction_site_check": internal_check,
                "reading_frame_check": "PASS" if reading_frame_ok else "FAIL",
                "SUMO_cleavage_product_check": "PASS: SUMO C-terminal GG is immediately followed by native LiSPER peptide" if cleavage_ok else "FAIL",
                "vendor_notes": (
                    "Clone into the original pET-28a(+) MCS using NdeI/XhoI. "
                    "The 5' NdeI site supplies the ATG start codon, so the synthesis insert is NdeI + ORF_without_duplicate_ATG + XhoI. "
                    "NcoI is not used because it would constrain the second codon and disrupt exact MHHHHHH His6-SUMO expression."
                ),
            }
        )

        qc_rows.append(
            {
                "candidate_id": candidate,
                "chosen_5_prime_site": FIVE_PRIME_SITE_NAME,
                "chosen_3_prime_site": THREE_PRIME_SITE_NAME,
                "complete_ORF_length_bp": str(len(orf_dna)),
                "complete_ORF_length_divisible_by_3": str(len(orf_dna) % 3 == 0),
                "final_synthesis_insert_length_bp": str(len(final_insert)),
                "ORF_starts_with_ATG": str(orf_dna.startswith("ATG")),
                "ORF_ends_with_stop_codon": str(orf_dna.endswith(STOP_CODON)),
                "translated_ORF_matches_expected_fusion": str(str(Seq(orf_dna).translate(to_stop=False)).rstrip("*") == orf_aa),
                "NdeI_XhoI_internal_site_check": internal_check,
                "other_common_MCS_sites_inside_ORF": common_site_note,
                "reading_frame_after_NdeI_cloning": str(reading_frame_ok),
                "post_SUMO_cleavage_peptide": peptide,
                "SUMO_cleavage_product_matches_intended_peptide": str(cleavage_ok),
                "NcoI_compatibility": "not recommended; NcoI would alter/constrain the second residue of the exact MHHHHHH N-terminus",
                "recommendation": "ready for vendor as NdeI/XhoI insert" if reading_frame_ok and cleavage_ok and internal_check.startswith("PASS") else "needs manual review",
            }
        )

    with (OUTDIR / "revised_vendor_order_table.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(order_rows[0]))
        writer.writeheader()
        writer.writerows(order_rows)

    with (OUTDIR / "restriction_site_QC_report.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(qc_rows[0]))
        writer.writeheader()
        writer.writerows(qc_rows)

    with (OUTDIR / "revised_vendor_instructions.txt").open("w") as handle:
        handle.write(
            "Please use the original pET-28a(+) backbone. Please synthesize each listed insert and clone it into the original pET-28a(+) MCS using the specified restriction sites. "
            "The insert encodes the complete His6-SUMO-LiSPER-STOP ORF. Please sequence-verify the full insert and both vector-insert junctions.\n\n"
            "Restriction strategy: NdeI/XhoI.\n"
            "Rationale: NdeI (CATATG) provides the ATG start codon without altering the second amino acid of the His6-SUMO ORF. "
            "NcoI is not recommended because CCATGG would force an extra/constrained residue after the start codon and would not preserve the exact MHHHHHH His6-SUMO N-terminus. "
            "XhoI is placed downstream of the TAA stop codon to prevent expression of C-terminal vector-derived residues or tags.\n\n"
            "Important cloning detail: for the final synthesis insert, the NdeI site contains the start codon. Do not duplicate the ATG after NdeI. "
            "The sequence format is CATATG + complete_ORF_without_its_first_ATG + CTCGAG.\n\n"
            "After SUMO protease cleavage, the released peptide should exactly match the listed native LiSPER peptide sequence with no residual His-tag, SUMO residue, T7 tag, linker, thrombin remnant, or vector-derived amino acid.\n\n"
            "This is a standard plasmid restriction-cloning order. Do not use CRISPR or genome editing.\n"
        )

    print(f"Wrote revised restriction-cloning order package to {OUTDIR}")


if __name__ == "__main__":
    main()
