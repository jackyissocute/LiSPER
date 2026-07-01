#!/usr/bin/env bash
set -eo pipefail
export PATH=$HOME/.local/bin:$PATH
export OMP_NUM_THREADS=1
cd "/mnt/lisper_data/LiSPER_remote/LiSPER_8cand_LiCl/systems/LiDA-1/gromacs/umbrella_sampling_binding_site_v2/v3_tail_repair_20260701_1105/window_026_extend_2ns"
gmx mdrun -s umbrella_ext.tpr -deffnm umbrella_ext -cpi "/mnt/lisper_data/LiSPER_remote/LiSPER_8cand_LiCl/systems/LiDA-1/gromacs/umbrella_sampling_binding_site_v2/window_026_2.08nm/umbrella.cpt" -noappend -ntmpi 1 -ntomp 1
