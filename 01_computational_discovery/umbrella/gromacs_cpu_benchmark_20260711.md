# GROMACS CPU benchmark — 2026-07-11

Host: GCP `lisper-runner-32v`, e2-highcpu-32, 32 vCPUs (16 AMD EPYC 7B12 cores with SMT), GROMACS 2026.0, AVX2_256.

Input: completed LiDA-1/LiCl umbrella window `window_013_1.10nm/umbrella.tpr`. Each isolated run started from the same TPR and ran 10,000 steps (20 ps) in `/tmp`; no production output or checkpoint was used or modified. The node retained 23–24 background one-thread `mdrun` jobs during the sequential benchmark.

| Allocation | ns/day | Wall time | Scaling efficiency vs 1 vCPU | GROMACS thread occupancy |
|---:|---:|---:|---:|---:|
| 1 vCPU | 4.615 | 374.499 s | 100.0% | 100.0% |
| 2 vCPU | 6.082 | 284.159 s | 65.9% | 100.0% |
| 4 vCPU | 10.729 | 161.071 s | 58.1% | 100.0% |
| 8 vCPU | 18.787 | 91.986 s | 50.9% | 100.0% |

Scaling efficiency is `(ns/day at N vCPU) / (N × 4.615 ns/day)`. GROMACS thread occupancy is `Core t / (Wall t × N)`; it shows that threads remained busy, not that additional threads scaled linearly.

## Recommendation

Use one vCPU per umbrella window (`-nt 1`, or explicitly `-ntmpi 1 -ntomp 1`) and parallelize across independent windows. At the measured rates, idealized aggregate throughput is 147.7, 97.3, 85.8, and 75.1 ns/day for 32×1, 16×2, 8×4, and 4×8-vCPU layouts, respectively.

Operationally keep the node at 28–30 simultaneous one-thread `mdrun` jobs, leaving 2–4 vCPUs for SSH, filesystem work, WHAM, and monitoring. Every umbrella `mdrun` uses `-ntmpi 1 -ntomp 1`. The 8-vCPU test briefly raised load to about 30.4, so its result represents the real near-saturation condition rather than an idle-node benchmark.

## Campaign scheduler

The umbrella driver now applies a node-wide locked ceiling of 28 real `gmx mdrun` processes. Per-track workers default to a queue depth of four, so capacity released by a nearly complete track can be consumed by tracks with longer backlogs without changing the one-thread-per-window allocation. Explicit supplemental windows use the same ceiling and are restricted to prepared, incomplete window directories.

During the 2026-07-11 transition, the legacy static allocation had fallen to 21 real jobs because NaCl LiD3-Flex had only one window remaining. Seven guarded far-end windows from longer LiCl/NaCl backlogs were started and one reserve was allowed to wait on the global gate, bringing the node to 28 real jobs with all commands conforming to `-ntmpi 1 -ntomp 1`.
