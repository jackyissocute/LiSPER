# Protocol Drafting Notes from Literature (Track A)

Short extraction of what to do with vendor peptides. Expand later into formal protocols under `02_experimental_validation/track_A_purified_peptide/protocols/`.

## Step 0 — Receipt / QC

From vendor certificate + TFA literature (`06_`):

1. Match vial sequence to order table.
2. File HPLC + MS.
3. Prefer TFA-removed / acetate or HCl form. If TFA salt: exchange before ion assays (AAPPTec bulletin; Guzmán 2025; Neelakantan 2012).
4. Reconstitute in low-Na buffer (pH with KOH, not NaOH).
5. Blank ICP of reconstituted peptide + buffer.

## Step 1 — Primary assay (beads)

From Bhargawa 2024 (`02_`):

1. Conjugate each of 8 peptides to same bead chemistry (EDC/NHS).
2. Quantify loading.
3. Incubate with Li-only, Na-only, Li+Na competition.
4. Magnetically separate; wash once with defined buffer; acid-elute bound ions.
5. ICP Li and Na.
6. Always include empty beads + `LiA3-Ref`.

## Step 2 — Optional free-solution confirmation

From Adams 2026 Chem Sci (`03_`):

1. Dialysis of top 2–3 hits vs Li, Na, and 1:1 mix.
2. ICP external dialysate before/after.
3. Confirm peptide does not leak through membrane.

## Step 3 — Rank vs PMF

1. Compute α_Li/Na at fixed competition condition (e.g. 1 mM Li + 100 mM Na).
2. Rank peptides.
3. Spearman vs computational ΔΔG / PMF rank.
4. Advance top hits to Track B display literature (`07_`).

## Controls that make the paper reliable

| Control | Why |
|---|---|
| No peptide / empty beads | Background sorption |
| `LiA3-Ref` | Low-donor negative reference |
| Buffer blank ICP | Contamination |
| Equal ionic-strength Na vs Li arms | Avoid charge-only artifacts |
| Independent peptide aliquots | True replication |
