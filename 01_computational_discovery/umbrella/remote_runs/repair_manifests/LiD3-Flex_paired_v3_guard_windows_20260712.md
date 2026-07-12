# LiD3-Flex paired V3 endpoint-guard repair

| Field | Value |
|---|---|
| Candidate-condition | LiD3-Flex LiCl / NaCl |
| Previous protocol | V2, 27 base windows |
| New protocol | V3, 27 analysis windows plus 3 endpoint guards per ion |
| Windows | `027`, `028`, `029`, sequential, `0.075 nm` spacing |
| Scientific reason | V2 WHAM places four NaCl poor-sampling bins beyond the final restraint center, where only window 026 contributes |
| Expected improvement | Move the finite-range artifact into guard-only space and protect a shared, overlapped reference plateau |
| NaCl action | Launch guards now from completed window 026 |
| LiCl action | Queue guards until active base windows 025-026 complete |
| Remote output | Existing `umbrella_sampling_binding_site_v2/window_027-*` through `window_029-*` directories |
| Completion signal | `Finished mdrun` in each guard `umbrella.log` plus `endpoint_guard_manifest.tsv` reporting three complete guards |
| Post-run QC | Paired full/burn-in/independent-half WHAM, interior overlap, plateau flatness, bootstrap uncertainty, then PASS/REPAIR |

Launch command uses `run_endpoint_guard_windows.py`; every `mdrun` remains `-ntmpi 1 -ntomp 1` behind the node-wide process gate.
