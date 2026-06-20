# Worker A NaCl Backfill Status

Last updated: 2026-06-20 23:41 CST

## Purpose

`LiDA-1` LiCl production completed and clustering produced a representative structure on Worker A, freeing two CPU slots. The two NaCl candidates that were queued behind Worker B's six active jobs were moved to Worker A as backfill jobs.

## Current Backfill Jobs

| Candidate | State |
|---|---|
| `LiND-Hybrid` | Active on Worker A backfill; `0.57 ns / 20 ns`; `-ntomp 1` |
| `LiN3-Core` | Active on Worker A backfill; `0.76 ns / 20 ns`; `-ntomp 1` |

## Scheduling Note

Worker A now runs seven LiCl production jobs at 2 threads each plus two NaCl backfill jobs at 1 thread each, filling the 16-core quota without duplicating Worker B. Worker B continues six NaCl production jobs at 2 threads each, filling its 12-core quota.
