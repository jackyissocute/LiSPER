# ICP-OES / ICP-MS Guidance for Track A Li⁺/Na⁺ Assays

Curated notes for LiSPER Track A protocol writing. Not a substitute for your core facility SOP.

## Role in Track A

| Method | Use |
|---|---|
| ICP-OES | Preferred routine quantification of Li and Na in feed, supernatant, wash, eluate, or dialysate |
| ICP-MS | Lower concentrations / residual metal blanks |
| Ion chromatography | Acceptable alternative if ICP unavailable and method validated for Li/Na |

## Sample types you will generate

1. Assay buffer blanks (KOH-HEPES/PIPES — check Li/Na background)
2. Reconstituted peptide blanks (detect vendor salt carryover)
3. No-peptide bead / tube controls
4. Li-only incubations
5. Na-only incubations
6. Li+Na competition mixtures
7. Bound-fraction eluates (acid strip from beads)

## Practical rules

1. **Acid matrix:** dilute samples into the same acid used for calibration (commonly ~1–2% HNO₃). Confirm peptide-acid compatibility for eluates.
2. **Calibration:** multi-point Li and Na curves bracketing expected concentrations; include independent QC standard.
3. **Dilution:** bring high-Na competition samples into linear range. High Na/Li ratios can bias some Li measurements — dilute and/or use matrix-matched standards.
4. **Mass balance:** when possible, check feed ≈ supernatant + wash + eluate (within recovery tolerance).
5. **Blanks every batch:** buffer, empty beads, `LiA3-Ref`, no-peptide tube.

## Selectivity calculation (from Track A analysis plan)

```text
q_Li = µmol Li bound / µmol peptide (or / mg bead)
q_Na = µmol Na bound / µmol peptide
α_Li/Na = (q_Li / q_Na) / (C_Li_feed / C_Na_feed)
```

If `q_Na` near LOD, report lower-bound selectivity using Na detection limit.

## Citable method context

| Topic | Reference | DOI |
|---|---|---|
| Dialysis + ICP-OES Li/Na uptake | Adams et al., *Chem. Sci.* 2026 | 10.1039/D6SC01183G |
| Bead adsorption + Li quantification | Bhargawa et al., *Desalination* 2024 | 10.1016/j.desal.2024.117412 |
| Li measurement / Na matrix awareness | Doherty et al., *JAAS* (Li isotopes; matrix discussion) | 10.1039/b907122a |

Store campus-library PDFs here when obtained:

```text
04_reference_library/Track A_Peptide Assay/04_icp_oes_ms_ion_quantification/
```

## Facility checklist before first assay day

- [ ] Book ICP-OES/MS time
- [ ] Confirm Li and Na lines / isotopes used by facility
- [ ] Confirm detection limits in your buffer matrix
- [ ] Confirm sample volume / tube type requirements
- [ ] Prepare labeled dilution scheme for competition arms (1 mM Li + 1/10/100 mM Na)
