#!/usr/bin/env bash
cd /root/LiSPER_remote
exec python3 /root/LiSPER_remote/run_lisper_equilibrate.py > /root/LiSPER_remote/equilibration_batch.nohup.log 2>&1
