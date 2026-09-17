"""Reconstruct and check the eight pET-11a designs; optional temporary GenBank export.

Run with an installed Biopython Python: python check_designs.py [--export-dir DIR]
"""
import argparse
import copy
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from Bio import SeqIO
from Bio.Restriction import BamHI, NdeI
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio.SeqRecord import SeqRecord

ROOT = Path(__file__).resolve().parent
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def designs():
    reference = SeqIO.read(ROOT / "pET-11a.dna", "snapgene")
    original = SeqIO.read(ROOT / "sources/GenScript_pET11a.fasta", "fasta").seq.upper()
    assert reference.seq == original and len(original) == 5677 and str(reference.seq).isupper()
    assert NdeI.search(original, linear=False) == [108]
    assert BamHI.search(original, linear=False) == [146]
    scaffold = SeqIO.read(ROOT / "sources/eCPX_scaffold_precursor.fasta", "fasta").seq.upper()
    omp = SeqIO.read(ROOT / "sources/OmpX_P0A917.fasta", "fasta").seq
    signal, leader, nlink, core = scaffold[:69], scaffold[69:84], scaffold[84:102], scaffold[102:-3]
    assert signal.translate() == omp[:23]
    assert leader.translate() == "GQSGQ" and nlink.translate() == "GGQSGQ"
    mature = str(omp[23:])
    core_expected = mature[53:] + "GSKSRR" + mature[:53]
    core_expected = core_expected[:88] + "LS" + core_expected[90:]
    assert str(core.translate()) == core_expected and len(core) == 462
    peptides = {r.id: str(r.seq) for r in SeqIO.parse(ROOT / "sources/candidates.fasta", "fasta")}
    assert peptides["LiDA-1"] == "DADGPGDPDAG"
    assert peptides["LiND-Hybrid"] == "GPGNPGSGPGDPGSGPGNP"
    codons = {"D": "GAC", "A": "GCT", "G": "GGT", "P": "CCG", "N": "AAC", "S": "TCT"}
    result = []
    his = Seq("CATCACCATCACCATCAC")
    assert str(his.translate()) == "HHHHHH"
    for peptide_name, side, tag_side in [("LiDA-1", "N", "C"), ("LiDA-1", "C", "N"), ("LiND-Hybrid", "N", "C"), ("LiND-Hybrid", "C", "N"), (None, None, None), (None, None, "N"), (None, None, "C")]:
        name = f"pET11a_{peptide_name}_{side}" if side else "pET11a_Empty_eCPX"
        if not side and tag_side:
            name += f"_{tag_side}-His6"
        peptide = peptides[peptide_name] if peptide_name else ""
        peptide_dna = Seq("".join(codons[aa] for aa in peptide))
        modules = [("OmpX signal peptide", signal, "#E6B800"), ("N-display leader (GQSGQ)", leader, "#66CCCC")]
        if tag_side == "N":
            modules.append(("His6 (N-side)", his, "#0080FF"))
        if side == "N":
            modules.append((f"{peptide_name} N-display", peptide_dna, "#D95F59"))
        modules += [("N-display linker (GGQSGQ)", nlink, "#66CCCC"), ("eCPX core", core, "#63A35C"), ("C-display linker (GGS)", Seq("GGTGGTTCT"), "#66CCCC")]
        if side == "C":
            modules.append((f"{peptide_name} C-display", peptide_dna, "#D95F59"))
        if tag_side == "C":
            modules.append(("His6 (C-side)", his, "#0080FF"))
        modules.append(("Stop codon (TAA)", Seq("TAA"), "#888888"))
        cds = sum((dna for _, dna, _ in modules), Seq(""))
        protein = str(cds.translate(to_stop=True))
        assert str(cds.translate()).count("*") == 1 and cds[-3:] == "TAA"
        assert protein.count("HHHHHH") == int(bool(tag_side))
        if tag_side == "N":
            assert protein.startswith(str(signal.translate()) + "GQSGQHHHHHHGGQSGQ")
        if tag_side == "C":
            assert protein.endswith("GGSHHHHHH")
        if side == "C":
            assert protein.endswith("GGS" + peptide)
        if side == "N":
            assert protein.startswith(str(signal.translate()) + "GQSGQ" + peptide + "GGQSGQ")
        final = original[:108] + cds + original[144:]
        donor = Seq("CAT") + cds + Seq("GGATCC")
        assert NdeI.search(donor) == [3] and BamHI.search(donor) == [len(donor) - 4]
        assert original[:107] + donor[2:len(donor)-5] + original[145:] == final
        assert NdeI.search(final, linear=False) == [108]
        assert BamHI.search(final, linear=False) == [len(cds) + 110]
        record = SeqRecord(final, id=name, name=name, description=f"eCPX {peptide_name or 'empty control'} {side or ''} display in pET-11a; {tag_side + '-side His6' if tag_side else 'tag-free'}")
        record.annotations = {"molecule_type": "DNA", "topology": "circular", "date": "16-SEP-2026", "comment": "GenScript pET-11a ID 47; unchanged bp-1 origin and forward T7 expression. NdeI/BamHI replace original bp 109-144, rebuilding boundary sites bp 106-150. Designed, not experimentally validated. BL21(DE3) or another T7-RNAP host required. eCPX geometry: Getz 2012; Kenrick 2009/2010. Backbone annotations from www.snapgene.com/resources."}
        delta = len(cds) - 36
        for feature in reference.features:
            label = feature.qualifiers.get("label", [""])[0]
            if label == "T7 tag":
                continue
            f = copy.deepcopy(feature)
            if int(f.location.start) >= 144:
                f.location = f.location + delta
            assert f.extract(final) == feature.extract(original)
            record.features.append(f)

        def mark(a, b, label, color, kind="misc_feature", note=""):
            qualifiers = {"label": [label], "ApEinfo_fwdcolor": [color], "ApEinfo_revcolor": [color]}
            if note:
                qualifiers["note"] = [note]
            record.features.append(SeqFeature(SimpleLocation(a, b, strand=1), type=kind, qualifiers=qualifiers))

        record.features.append(SeqFeature(SimpleLocation(108, 108 + len(cds), strand=1), type="CDS", qualifiers={"label": ["eCPX display CDS"], "codon_start": ["1"], "translation": [protein], "note": [f"Signal peptide first; {tag_side + '-side His6' if tag_side else 'tag-free'}; stop before BamHI. N-display retains GQSGQ leader: not a free terminal peptide N-terminus."], "ApEinfo_fwdcolor": ["#800080"]}))
        pos = 108
        for label, dna, color in modules:
            mark(pos, pos + len(dna), label, color, "sig_peptide" if label == "OmpX signal peptide" else "misc_feature", "Mature OmpX S54-F148 | GSKSRR | A1-S53; precursor A165L/G166S." if label == "eCPX core" else "")
            if label == "eCPX core":
                mark(pos + 264, pos + 270, "eCPX A165L/G166S", "#9673A6", note="Original OmpX precursor numbering; stabilizing substitutions.")
                mark(pos + 285, pos + 303, "Permutation linker (GSKSRR)", "#9673A6")
            pos += len(dna)
        mark(105, 111, "NdeI (5′ junction)", "#888888")
        mark(108 + len(cds), 114 + len(cds), "BamHI (3′ junction)", "#888888")
        result.append((record, str(donor), protein))
    return result


def check_saved(items):
    expected_names = {r.id + ".dna" for r, _, _ in items} | {"pET-11a.dna"}
    assert {p.name for p in ROOT.glob("*.dna")} == expected_names
    for record, _, protein in items:
        saved = SeqIO.read(ROOT / (record.id + ".dna"), "snapgene")
        assert saved.seq == record.seq and str(saved.seq).isupper()
        assert saved.annotations["topology"] == "circular"
        saved_features = {f.qualifiers.get("label", [""])[0]: f for f in saved.features}
        for f in record.features:
            label = f.qualifiers["label"][0]
            assert label in saved_features, (record.id, label)
            sf = saved_features[label]
            assert sf.location == f.location and sf.extract(saved.seq) == f.extract(record.seq), (record.id, label)
        cds = saved_features["eCPX display CDS"]
        assert str(cds.extract(saved.seq).translate(to_stop=True)) == protein
        print(f"PASS {record.id}: {len(saved)} bp; {len(protein)} aa; unique NdeI/BamHI; {len(saved.features)} features")
    with zipfile.ZipFile(ROOT / "pET11a_Synthesis.xlsx") as z:
        workbook = ET.fromstring(z.read("xl/workbook.xml"))
        assert [s.attrib["name"] for s in workbook.findall("s:sheets/s:sheet", NS)] == ["Synthesis"]
        sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
        assert not sheet.findall(".//s:f", NS), "Workbook must contain literal values, not formulas"
        shared = ET.fromstring(z.read("xl/sharedStrings.xml")) if "xl/sharedStrings.xml" in z.namelist() else None
        strings = ["".join(t.text or "" for t in si.findall(".//s:t", NS)) for si in shared] if shared is not None else []
        cells = {c.attrib["r"]: c for c in sheet.findall(".//s:c", NS)}
        def cell_text(c):
            if c.attrib.get("t") == "s":
                return strings[int(c.find("s:v", NS).text)]
            elif c.attrib.get("t") == "inlineStr":
                return "".join(t.text or "" for t in c.findall(".//s:t", NS))
            else:
                assert c.attrib.get("t") == "str", "DNA insert must be stored as text"
                return c.find("s:v", NS).text
        for record, donor, _ in items:
            rows = [address[1:] for address, c in cells.items() if address.startswith("A") and cell_text(c) == record.id]
            assert len(rows) == 1, (record.id, "Missing or duplicate Excel construct")
            assert cell_text(cells[f"C{rows[0]}"]) == donor, (record.id, "Excel insert differs")
    print("PASS eight DNA files; GenScript reference unchanged; all seven Excel insert sequences exact literals")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--export-dir", type=Path)
    args = parser.parse_args()
    items = designs()
    if args.export_dir:
        args.export_dir.mkdir(parents=True, exist_ok=True)
        for record, _, _ in items:
            path = args.export_dir / (record.id + ".gb")
            SeqIO.write(record, path, "genbank")
            prefix, origin = path.read_text().split("ORIGIN")
            path.write_text(prefix + "ORIGIN" + origin.upper())
        (args.export_dir / "inserts.json").write_text(json.dumps([{ "name": r.id, "insert": donor, "protein": protein, "bp": len(r)} for r, donor, protein in items], indent=2))
        print(f"PASS restriction ligation simulation and translation; exported seven constructs to {args.export_dir}")
    else:
        check_saved(items)
