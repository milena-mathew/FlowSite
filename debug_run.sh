#!/bin/bash
#
#SBATCH --job-name=flowsite_quick
#
##SBATCH -N 1
#SBATCH -n 1
#
#SBATCH --time=02:00:00
#SBATCH --begin=now+0days
#SBATCH -p deissero
#SBATCH --gpus=1
#SBATCH --mem=16G
#
#SBATCH -o slurm/quick_request.out
#SBATCH -e slurm/quick_request.err
#SBTACH --no-requeue
#
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=jnoh2@stanford.edu

python debug.py --wandb --run_name short_test --run_test --checkpoint pocket_gen/duw71q7p/checkpoints/best.ckpt --batch_size 1 --predict_split_path index/timesplit_test --num_inference 10 --save_inference --save_all_batches --check_nan_grads --use_tfn --time_condition_tfn --correct_time_condition --time_condition_inv --time_condition_repeat --flow_matching --flow_matching_sigma 0.5 --prior_scale 1 --layer_norm --tfn_detach --max_lig_size 200 --num_workers 0 --check_val_every_n_epoch 1 --cross_radius 50 --protein_radius 30 --lig_radius 50  --ns 32 --nv 8 --tfn_use_aa_identities --self_condition_x --pocket_residue_cutoff_sigma 0.5 --pocket_center_sigma 0.2 --pocket_type ca_distance --pocket_residue_cutoff 14 --fake_ratio_start 1 --fake_ratio_end 1 --debug #--sidechain_alternate

#echo $(date)
