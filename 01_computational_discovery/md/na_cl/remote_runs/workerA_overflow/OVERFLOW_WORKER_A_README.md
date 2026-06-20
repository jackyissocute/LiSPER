# NaCl Overflow Worker A

This workdir runs the two NaCl candidates that were queued behind the six active NaCl jobs on Worker B.

- Source workdir: `/root/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker`
- Overflow candidates: `LiND-Hybrid`, `LiN3-Core`
- Launch strategy: 2 jobs x 1 OpenMP thread each, using the freed 2-core slot after LiDA-1 LiCl production completed on Worker A.
- Purpose: keep Worker A at 16/16 CPU without duplicating Worker B active jobs.
