# Worker A NaCl Backfill Status

Last updated: 2026-06-23 23:50 CST

## Purpose

`LiDA-1` LiCl production completed and clustering produced a representative structure on Worker A, freeing two CPU slots. The two NaCl candidates that were queued behind Worker B's six active jobs were moved to Worker A as backfill jobs.

## Current Backfill Jobs

| Candidate | State |
|---|---|
| `LiND-Hybrid` | Active on replacement Worker A backfill; `4.66 ns / 20 ns`; `-ntomp 1` |
| `LiN3-Core` | Active on replacement Worker A backfill; `7.10 ns / 20 ns`; `-ntomp 1` |

## Scheduling Note

Replacement Worker A now runs two LiCl production jobs at 2 threads each plus two NaCl backfill jobs at 1 thread each plus twelve LiCl umbrella windows at 1 thread each, using 18/18 cores without duplicating Worker B. Worker B continues three NaCl production jobs at 2 threads each, four `LiDS-1` NaCl umbrella windows at 1 thread each, and one `LiLC-1` NaCl pull at 1 thread, using 11/12 cores during the pull; it should return toward 12/12 when `LiLC-1` window mdruns begin.
