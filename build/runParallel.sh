#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --account=NAME_OF_THE_ACCOUNT
#SBATCH -t 0:26:01

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PROC_BIND=true
export OMP_PLACES=cores

echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"

mpirun -np 1 ./run_min > run.dump
