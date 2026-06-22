# Worker A NaCl Backfill Status

Last updated: 2026-06-22 09:10 CST

## Purpose

`LiDA-1` LiCl production completed and clustering produced a representative structure on Worker A, freeing two CPU slots. The two NaCl candidates that were queued behind Worker B's six active jobs were moved to Worker A as backfill jobs.

## Current Backfill Jobs

| Candidate | State |
|---|---|
| `LiND-Hybrid` | Active on Worker A backfill; `2.73 ns / 20 ns`; `-ntomp 1` |
| `LiN3-Core` | Active on Worker A backfill; `4.12 ns / 20 ns`; `-ntomp 1` |

## Scheduling Note

Worker A now runs six LiCl production jobs at 2 threads each plus two NaCl backfill jobs at 1 thread each plus two LiCl umbrella windows at 1 thread each, using 16/16 cores without duplicating Worker B. Worker B continues four NaCl production jobs at 2 threads each plus three `LiDA-1` NaCl umbrella windows at 1 thread each, using 11/12 cores after `LiDS-1` NaCl completed and clustered but blocked before umbrella window generation.
