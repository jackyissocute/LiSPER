"""Rebuild the six reference designs and verify translation, topology and junctions.

Requires Biopython. Run from any directory: python build_sequences.py
The input FASTA/GenBank records are frozen in sources/. No network required.
"""
from copy import deepcopy
import csv
import hashlib
import json
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio.SeqRecord import SeqRecord
from Bio.SeqUtils import molecular_weight

ROOT = Path(__file__).resolve().parent


def feature(start, end, label, kind="misc_feature", **qualifiers):
    return SeqFeature(SimpleLocation(start, end, strand=1), type=kind,
                      qualifiers={"label": [label], **{k: [v] for k, v in qualifiers.items()}})


def main():
    vendor = SeqIO.read(ROOT / "sources/GenScript_pET28a.fasta", "fasta")
    backbone = SeqIO.read(ROOT / "sources/pET28a_annotated_reference.gb", "genbank")
    source = SeqIO.read(ROOT / "sources/eCPX_scaffold_precursor.fasta", "fasta")
    native = str(SeqIO.read(ROOT / "sources/OmpX_P0A917.fasta", "fasta").seq)
    candidates = {r.id: str(r.seq) for r in SeqIO.parse(ROOT / "sources/candidates.fasta", "fasta")}
    assert candidates["LiDA-1"] == "DADGPGDPDAG"
    assert candidates["LiND-Hybrid"] == "GPGNPGSGPGDPGSGPGNP"
    assert len(vendor) == 5369 and vendor.seq.upper() == backbone.seq.upper()
    original = source.seq.upper()
    assert len(original) == 567
    aa = str(original.translate(cds=True))
    signal, prefix, nlink = aa[:23], aa[23:28], aa[28:34]
    core = aa[34:]
    assert len(aa) == 188 and len(core) == 154
    assert signal == native[:23] == "MKKIACLSALAAVLAFTAGTSVA"
    assert prefix == "GQSGQ" and nlink == "GGQSGQ"
    mutated = list(native)
    assert mutated[164:166] == ["A", "G"]
    mutated[164:166] = ["L", "S"]
    assert core == "".join(mutated[76:]) + "GSKSRR" + native[23:76]

    # Replace the native ATG through the MCS before XhoI, using seamless assembly.
    start, end = 107, 243  # 0-based half-open; vendor coordinates 108..243 inclusive
    s = str(backbone.seq).upper()
    assert s[start:start+3] == "ATG" and s[end:end+6] == "CTCGAG"
    assert s[105:111] == "CCATGG" and s[164:170] == "CATATG"
    left_arm, right_arm = s[start-30:start], s[end:end+30]
    codons = {"A": "GCT", "D": "GAT", "G": "GGT", "H": "CAT",
              "N": "AAC", "P": "CCG", "Q": "CAG", "S": "TCT"}
    encode = lambda protein: "".join(codons[x] for x in protein)
    modules = [
        ("OmpX signal peptide", str(original[:69]), signal),
        ("post-cleavage leader", str(original[69:84]), prefix),
        ("N-terminal peptide", "", ""),
        ("N display linker", str(original[84:102]), nlink),
        ("eCPX core", str(original[102:-3]), core),
        ("C display linker", encode("GGQSGQ"), "GGQSGQ"),
        ("His6 detection tag", "CATCACCATCACCATCAC", "HHHHHH"),
        ("distal spacer", encode("GSG"), "GSG"),
        ("C-terminal peptide", "", ""),
    ]
    constructs = [("LiDA1_N", "LiDA-1", "N"), ("LiDA1_C", "LiDA-1", "C"),
                  ("LiND_N", "LiND-Hybrid", "N"), ("LiND_C", "LiND-Hybrid", "C"),
                  ("eCPX_only", "None", "Control")]
    for folder in ["genbank", "sequences"]:
        (ROOT / folder).mkdir(exist_ok=True)
    rows, inserts, proteins, complete = [], [], [], []
    for name, peptide_name, direction in constructs:
        ident = "pET28a_" + name
        peptide = candidates.get(peptide_name, "")
        parts = list(modules)
        if peptide:
            i = 2 if direction == "N" else 8
            parts[i] = (peptide_name + " " + direction + " display", encode(peptide), peptide)
        dna = "".join(x[1] for x in parts) + "TAA"
        protein = "".join(x[2] for x in parts)
        assert str(Seq(dna).translate(cds=True)) == protein
        assert protein.count("HHHHHH") == 1 and protein.count(core) == 1
        assert not peptide or protein.count(peptide) == 1
        assert protein.startswith(signal + prefix)
        assert direction != "C" or protein.endswith(peptide)
        assert direction != "N" or protein[28:28+len(peptide)] == peptide
        record = SeqRecord(Seq(s[:start] + dna + s[end:]), id=ident, name=ident,
                           description=f"LiSPER {peptide_name} {direction} eCPX display design; GenScript pET-28a(+)")
        record.annotations = {"molecule_type": "DNA", "topology": "circular",
                              "date": "08-SEP-2026", "comment": "Sequence-defined design, not experimentally validated. Vendor sequence origin retained. Seamless replacement of reference nt 108..243. BL21(DE3) expression host."}
        delta = len(dna) - (end-start)
        for f in backbone.features:
            a, b = int(f.location.start), int(f.location.end)
            if b <= start:
                record.features.append(deepcopy(f))
            elif a >= end:
                new = deepcopy(f)
                new.location = f.location + delta
                if f.qualifiers.get("label") == ["6xHis"]:
                    new.type = "misc_feature"
                    new.qualifiers = {"label": ["vector His6 DNA - untranslated"], "note": ["Upstream synthetic stop prevents fusion to the native vector C-terminal tag."]}
                record.features.append(new)
        record.features.append(feature(start, start+len(dna), "display fusion ORF", "CDS",
                                       codon_start="1", transl_table="11", translation=protein,
                                       product="eCPX surface-display fusion"))
        offset = start
        for label, nt, prot in parts:
            if nt:
                record.features.append(feature(offset, offset+len(nt), label,
                                               "sig_peptide" if label.startswith("OmpX signal") else "misc_feature",
                                               note=f"Protein sequence: {prot}"))
                offset += len(nt)
        record.features.append(feature(offset, offset+3, "synthetic stop TAA"))
        record.features.sort(key=lambda f: int(f.location.start))
        fragment = left_arm + dna + right_arm
        assert fragment[30:-30] == dna
        assert str(record.seq[:start]) == s[:start]
        assert str(record.seq[start+len(dna):]) == s[end:]
        assert str(record.seq[start-30:start+len(dna)+30]) == fragment
        assert str(record.seq).count("CTCGAG") == 1
        assert len(record) == 5369-136+len(dna)
        # Compare retained annotated backbone CDS nucleotides, not just plasmid size.
        for f in backbone.features:
            if f.type == "CDS" and int(f.location.start) >= end and f.qualifiers.get("label") != ["6xHis"]:
                kept = next(k for k in record.features if k.qualifiers.get("label") == f.qualifiers.get("label"))
                assert kept.extract(record.seq) == f.extract(backbone.seq)
        SeqIO.write(record, ROOT / "genbank" / (ident + ".gb"), "genbank")
        assert SeqIO.read(ROOT / "genbank" / (ident + ".gb"), "genbank").seq == record.seq
        inserts.append(SeqRecord(Seq(fragment), id=ident, description="synthesis fragment 5prime-to-3prime; 30bp left overlap + complete CDS including stop + 30bp right overlap"))
        proteins.append(SeqRecord(Seq(protein), id=ident, description="precursor; signal peptide residues 1-23 expected removed"))
        complete.append(record)
        rows.append(dict(id=ident, peptide=peptide_name, orientation=direction, backbone="GenScript pET-28a(+) 5369 bp",
                         peptide_aa=peptide, precursor_aa=protein, cds_dna=dna, synthesis_dna=fragment,
                         cds_bp=len(dna), synthesis_bp=len(fragment), plasmid_bp=len(record),
                         precursor_kda=round(molecular_weight(protein, seq_type="protein")/1000, 3),
                         mature_kda=round(molecular_weight(protein[23:], seq_type="protein")/1000, 3),
                         assembly="Seamless replacement of reference nt 108..243 (native ATG to before XhoI)",
                         strand="+ relative to GenScript reference; same transcription direction as T7",
                         arrangement=" - ".join(x[2] if x[0] != "eCPX core" else "eCPX(core154)" for x in parts if x[1]) + " - STOP",
                         left_arm=left_arm, right_arm=right_arm,
                         sha256=hashlib.sha256(str(record.seq).encode()).hexdigest()))
    empty = deepcopy(backbone)
    empty.id = empty.name = "pET28a_empty"
    empty.description = "Unmodified GenScript pET-28a(+) reference; empty-vector control"
    SeqIO.write(empty, ROOT / "genbank/pET28a_empty.gb", "genbank")
    complete.append(empty)
    rows.append(dict(id=empty.id, peptide="None", orientation="Empty vector", backbone="GenScript pET-28a(+) 5369 bp",
                     peptide_aa="", precursor_aa="", cds_dna="", synthesis_dna="", cds_bp=0, synthesis_bp=0,
                     plasmid_bp=len(empty), precursor_kda=None, mature_kda=None,
                     assembly="No synthesis or insertion; supply unmodified backbone", strand="Not applicable",
                     arrangement="Native pET-28a(+) expression region retained", left_arm="", right_arm="",
                     sha256=hashlib.sha256(str(empty.seq).encode()).hexdigest()))
    assert len(rows) == 6 and len(inserts) == 5 and len({x["sha256"] for x in rows}) == 6
    SeqIO.write(inserts, ROOT / "sequences/synthesis_fragments.fasta", "fasta")
    SeqIO.write([SeqRecord(Seq(r["cds_dna"]), id=r["id"], description="CDS including TAA; no assembly overlaps") for r in rows[:-1]], ROOT / "sequences/coding_sequences.fasta", "fasta")
    SeqIO.write(proteins, ROOT / "sequences/precursor_proteins.fasta", "fasta")
    SeqIO.write(complete, ROOT / "sequences/complete_plasmids.fasta", "fasta")
    (ROOT / "constructs.json").write_text(json.dumps(rows, indent=2) + "\n")
    with (ROOT / "constructs.tsv").open("w") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys(), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    report = ["# Sequence checks", "", "All assertions in build_sequences.py passed.", "",
              "Verified: source OmpX permutation S54–F148 / GSKSRR / A1–S53, A165L/G166S (precursor numbering), preserved native signal, candidate identity, CDS translation, single encoded His6, no internal stop, exact seamless junctions, intact retained backbone CDS sequences, GenBank round trips, five inserts and six distinct full plasmids.", "",
              "These are sequence checks. They do not establish export, membrane insertion, surface exposure, or lithium binding.", "",
              "| Plasmid | CDS bp | Synthesis bp | Plasmid bp | Precursor kDa | Predicted mature kDa |",
              "|---|---:|---:|---:|---:|---:|"]
    for r in rows:
        report.append(f"| {r['id']} | {r['cds_bp']} | {r['synthesis_bp']} | {r['plasmid_bp']} | {r['precursor_kda'] or 'n/a'} | {r['mature_kda'] or 'n/a'} |")
    (ROOT / "sequence_QC.md").write_text("\n".join(report) + "\n")
    print("PASS: six full plasmids, five synthesis fragments; all sequence assertions passed.")
    print("Assembly arms:", left_arm, right_arm)
    for row in rows:
        print(row["id"], row["synthesis_bp"], row["plasmid_bp"], row["mature_kda"])


if __name__ == "__main__":
    main()
