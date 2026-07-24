# Completed paired umbrella/PMF archive

Local snapshot of the completed LiCl/NaCl umbrella campaigns, assembled on
2026-07-25 CST from:

- `lisper-epyc:/data/LiSPER_remote/LiSPER_8cand_LiCl`
- `lisper-epyc:/data/LiSPER_remote/LiSPER_8cand_NaCl_prod_worker`
- `lisper-epyc:/data/LiSPER_remote/paired_pmf`

## Layout

| Path | Contents |
| --- | --- |
| `campaigns/LiCl/<candidate>/` | LiCl GROMACS inputs, logs, coordinates, force/position series, pulling trajectory, and locally retained restart data |
| `campaigns/NaCl/<candidate>/` | Matching NaCl campaign files |
| `paired_pmf/<candidate>/<ion>/` | Complete WHAM profiles, histograms, ACF/IACT evidence, bootstrap outputs, sensitivity variants, logs, and input lists |
| `workflow/` | Exact remote scripts, locked paired-site definitions, and orchestration logs |
| `manifest/` | Remote catalogs, local bulk-data coverage, and SHA-256 checksums |

The guaranteed campaign reproduction set was compared file-by-file with the
remote source and includes all `TPR`, `MDP`, `GRO`, topology/index files,
production and equilibration logs, and `pullf`/`pullx` XVG series. It contains
480/480 production TPR/pull-force pairs. All 480 EQ and 480 production logs
verify their configured final `nsteps` and `Finished mdrun`.

`paired_pmf/` is an exact 578-file mirror. It contains 16 complete ion-level
WHAM sets and eight paired-QC rows. `delta_g_summary.tsv` and
`selectivity_summary.tsv` are byte-identical to the tracked final tables under
`01_computational_discovery/pmf/`.

## Large trajectory coverage

The remote campaign trees total about 196.7 GiB and contain about 200.0 GB of
XTC trajectories, while only about 13 GiB was free locally during this
snapshot. Copying every trajectory would have been unsafe.

All 16 pulling XTCs are local. The prior restart snapshot also supplies a
useful but explicitly partial set of window trajectories, checkpoints, and
energy files. Exact local-versus-remote counts and byte totals are in
`manifest/bulk_data_coverage.tsv`. Every remote bulk file is listed in
`manifest/remote_bulk_file_catalog.tsv`; the complete campaign inventory is in
`manifest/remote_campaign_file_catalog.tsv`.

The remote files remain authoritative for any missing EQ/production XTC,
checkpoint, or energy file. Retrieve a needed file into its matching campaign
path, for example:

```bash
rsync -avP \
  lisper-epyc:/data/LiSPER_remote/LiSPER_8cand_LiCl/systems/<candidate>/gromacs/umbrella_sampling/window_<id>/umbrella.xtc \
  campaigns/LiCl/<candidate>/gromacs/umbrella_sampling/window_<id>/
```

## Analysis notes

- The reported estimand is the radially corrected, endpoint-referenced,
  within-protocol PMF binding difference:
  `Delta Delta G = Delta G(Li) - Delta G(Na)`.
- Negative values indicate nominal Li preference. These are not 1 M standard
  binding free energies.
- Guard windows are excluded from the reference region.
- The `tpr-files.dat` and `pullf-files.dat` files preserve the original remote
  absolute paths. Rewrite those paths to this local mirror before rerunning
  WHAM locally; do not edit the archived originals.
- Treat `campaigns/` as read-only. Most files are hard-linked to the existing
  local restart backup to avoid duplicating tens of gigabytes. Copy files to a
  separate working directory before modifying them.

Verify the local archived data with:

```bash
(cd 01_computational_discovery/umbrella/analysis_archive_20260725 && \
  shasum -a 256 -c manifest/local_file_checksums.sha256)
```

The bulk archive directories are intentionally ignored by Git; this README and
the manifests are tracked so the local data remain discoverable without
putting simulation binaries or trajectories into GitHub.
