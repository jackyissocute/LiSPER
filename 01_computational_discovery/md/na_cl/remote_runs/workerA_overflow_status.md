# Worker A NaCl Backfill Status

Last updated: 2026-06-22 22:12 CST

## Purpose

`LiDA-1` LiCl production completed and clustering produced a representative structure on Worker A, freeing two CPU slots. The two NaCl candidates that were queued behind Worker B's six active jobs were moved to Worker A as backfill jobs.

## Current Backfill Jobs

| Candidate | State |
|---|---|
| `LiND-Hybrid` | Active on replacement Worker A backfill; `3.49 ns / 20 ns`; `-ntomp 1` |
| `LiN3-Core` | Active on replacement Worker A backfill; `5.27 ns / 20 ns`; `-ntomp 1` |

## Scheduling Note

Replacement Worker A now runs six LiCl production jobs at 2 threads each plus two NaCl backfill jobs at 1 thread each plus four LiCl umbrella windows at 1 thread each, using 18/18 cores without duplicating Worker B. Worker B continues four NaCl production jobs at 2 threads each plus four `LiDA-1` NaCl umbrella windows at 1 thread each, using 12/12 cores.
