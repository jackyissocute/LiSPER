# Worker A NaCl Backfill Status

Last updated: 2026-06-24 09:28 CST

## Purpose

`LiDA-1` LiCl production completed and clustering produced a representative structure on Worker A, freeing two CPU slots. The two NaCl candidates that were queued behind Worker B's six active jobs were moved to Worker A as backfill jobs.

## Current Backfill Jobs

| Candidate | State |
|---|---|
| `LiND-Hybrid` | Active on replacement Worker A backfill; `5.09 ns / 20 ns`; `-ntomp 1` |
| `LiN3-Core` | Active on replacement Worker A backfill; `7.78 ns / 20 ns`; `-ntomp 1` |

## Scheduling Note

Replacement Worker A now runs two LiCl production jobs at 2 threads each plus two NaCl backfill jobs at 1 thread each plus twelve LiCl umbrella windows at 1 thread each, using 18/18 cores without duplicating Worker B. Worker B now has one NaCl production job, two `LiLC-1` NaCl windows, and two new NaCl pulls (`LiA3-Ref`, repaired `LiD3-Core`); it should ramp as those pulls convert into one-thread umbrella windows.
