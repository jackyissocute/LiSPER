#!/usr/bin/env bash
set -euo pipefail
export PATH=$HOME/.local/bin:$PATH
export OMP_NUM_THREADS=1
export GMX_MAXBACKUP=-1
cd /mnt/lisper_data/LiSPER_remote/LiSPER_8cand_LiCl/systems/LiDA-1/gromacs/umbrella_sampling_binding_site_v2/v4_tail_repair_20260702_0256/window_026_extend_to_6ns
gmx mdrun -s umbrella_v4.tpr -deffnm umbrella_v4 -cpi /mnt/lisper_data/LiSPER_remote/LiSPER_8cand_LiCl/systems/LiDA-1/gromacs/umbrella_sampling_binding_site_v2/v3_tail_repair_20260701_1105/window_026_extend_2ns/umbrella_ext.cpt -noappend -ntmpi 1 -ntomp 1
