# QuickPod primary compute (2026-07-12)

Primary MD/umbrella worker after GCP soft-stop migration.

| Item | Value |
|---|---|
| SSH | `ssh quickpod-lisper` (`root@217.254.101.12 -p 63014`) |
| CPU | 126 threads, AMD EPYC 7773X |
| Disk | 100 GB (`/` ≈ 96G usable) |
| GROMACS | `/opt/gromacs/2026.0/bin/gmx` (2026.0, AVX2_256) |
| Remote root | `/data/LiSPER_remote` |
| LiCl workdir | `/data/LiSPER_remote/LiSPER_8cand_LiCl` |
| NaCl prod workdir | `/data/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker` |
| NaCl overflow | `/data/LiSPER_remote/LiSPER_8cand_NaCl_overflow_workerA` |
| Scripts | `/data/LiSPER_remote/scripts` |
| Site manifests | `/data/LiSPER_remote/paired_binding_sites` |
| Resume launcher | `resume_incomplete_windows_quickpod.py` |
| Job layout | 1 thread / window (`-ntmpi 1 -ntomp 1`), cap `LISPER_GLOBAL_MDRUN_LIMIT=120` |

Do not use GCP paths (`/mnt/lisper_data/...`) on this host.

Scientific note: finishing existing `umbrella_sampling_binding_site_v2` windows uses the legacy dynamic-nearest site definition and remains **diagnostic** for paired ΔΔG until locked-site `VALIDATED_BOUND` campaigns complete. Promotion hold stays active.
