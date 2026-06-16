# NaCl Remote GROMACS Status

Last checked: 2026-06-16 11:27 CST

Host: connect.westb.seetacloud.com
Port: 37049
Remote root: /root/LiSPER_remote
Remote NaCl workdir: /root/LiSPER_remote/LiSPER_NaCl
GROMACS env: conda activate lisper-gmx
GROMACS version: 2026.0-conda_forge
Disk status: 30G total, 5.7G used, 25G available, 19% used.

Local QC:

- 10 NaCl systems are ready for GROMACS.
- LiD3-1 and StrongBind-Li were updated with revised CHARMM-GUI archives that include the `gromacs/` input-generator folder.

Pending:

- Sync summaries and per-system outputs back into this folder after the batch finishes.

Running:

- Uploaded the 8 ready NaCl systems to `/root/LiSPER_remote/LiSPER_NaCl`.
- Launched remote NaCl batch on 2026-06-14.
- Batch PID file: `/root/LiSPER_remote/LiSPER_NaCl/remote_runs/nacl_batch.pid`.
- Batch log: `/root/LiSPER_remote/LiSPER_NaCl/remote_runs/nacl_batch.log`.
- Historical launch observed PID `1609`; this originally used a NaCl-specific minimization script. Current orchestration has been consolidated to shared `run_lisper_minimize.py` with `LISPER_WORKDIR=/root/LiSPER_remote/LiSPER_NaCl`.
- Minimization completed successfully for all 8 ready NaCl systems.
- `IDP-Li-1`, `IDP-Li-2`, and `SoftCage-Li` each required one overlapping TIP3 water removal before successful minimization.
- Step4.1 equilibration completed for all 10 NaCl systems.
- Current local snapshot: `/Users/jackylin/Documents/GitHub/LiSPER/01_computational_discovery/md/na_cl/remote_runs/current_remote_snapshot.md`.
- Completed equilibration logs/results have been synced for all 10 NaCl systems.
- Uploaded revised NaCl LiD3-1 and StrongBind-Li systems to the remote.
- Updated remote `ready_gromacs_systems.tsv` now contains all 10 NaCl systems.
- Queued `/root/LiSPER_remote/queue_nacl_add2.py` with `WAIT_FOR_PID=1609`.
- Add-two queue PID file: `/root/LiSPER_remote/LiSPER_NaCl/remote_runs/nacl_add2_queue.pid`.
- Add-two queue completed for `LiD3-1` and `StrongBind-Li`.
- Queued `/root/LiSPER_remote/run_lisper_production_cluster.py` for all 10 NaCl systems with `WAIT_FOR_PID=3882`, so it starts after LiCl production/clustering.
- Production/clustering queue PID file: `/root/LiSPER_remote/LiSPER_NaCl/remote_runs/nacl_production_cluster_20ns.pid`.
- Latest observed NaCl production/clustering queue process: PID `72320`, still waiting for LiCl production/clustering to finish as of 2026-06-16 11:27 CST.
- This NaCl waiter was restarted with the patched shared production/clustering script, so it should use the corrected topology-path and peptide-only clustering logic when released.
- LiCl production/clustering is currently running active `StrongBind-Li` production at 17.87 ns / 20 ns; NaCl has not started production yet.
- No NaCl production or clustering outputs are expected until the LiCl queue exits.
- Production length: 20 ns per system (`nsteps = 10000000`, `dt = 0.002 ps`).
- Clustering method: `gmx cluster`, GROMOS method, SOLU RMSD group, cutoff 0.20 nm.
