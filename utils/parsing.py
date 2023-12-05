import sys
from argparse import ArgumentParser


def parse_train_args(args=sys.argv[1:]):
    parser = ArgumentParser()
    # Logging
    parser.add_argument('--warn_with_traceback', action='store_true', default=False, help='')
    parser.add_argument('--run_name', type=str, default='default', help='')
    parser.add_argument('--wandb', action='store_true', default=False, help='Whether or not to use wandb for logging')
    parser.add_argument('--project', type=str, default='pocket_gen', help='The name of the wandb project')
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('--print_freq', type=int, default=50, help='')
    parser.add_argument('--check_val_every_n_epoch', type=int, default=1, help='')
    parser.add_argument("--limit_train_batches", type=int, default=None)
    parser.add_argument("--limit_test_batches", type=int, default=None)
    parser.add_argument("--limit_val_batches", type=int, default=None)
    parser.add_argument("--check_unused_params", action="store_true")
    parser.add_argument("--check_nan_grads", action="store_true")
    parser.add_argument('--save_inference', action='store_true', default=False, help='Whether or not to save the generated complex structures when running inference during validation.')
    parser.add_argument("--save_all_batches", action="store_true", default=False, help='Whether or not to save all the generated complex structures or just the first batch when running prediction or validation.')
    parser.add_argument('--inference_save_freq', type=int, default=10, help='How often to save the generated complexes when running inference during validation.')

    # Inference
    parser.add_argument('--out_dir', type=str, default='data/inference_out', help='Path to output directory.')
    parser.add_argument('--num_inference', type=int, default=1, help='How many sequences to generate for each complex.')
    parser.add_argument('--csv_file', type=str, default=None, help='Path to a CSV file where you can specify the inputs below for multiple complexes.')
    parser.add_argument('--ligand', type=str, default=None, help='Path to a ligand file. Either this or the smiles must be specified.')
    parser.add_argument('--smiles', type=str, default=None, help='Ligand as smiles string. Either this or the ligand as path must be specified')
    parser.add_argument('--protein', type=str, default=None, help='Path to a protein file')
    parser.add_argument('--design_residues', type=str, default=None, help='String in the format like this where we first have the chain ID and then the residue number(s): "A60-65,A232,A233,B212-215,B325"')

    parser.add_argument('--pocket_def_ligand', type=str, default=None, help='Path to a ligand file via which the pocket should be specified in the Distance pocket definition')
    parser.add_argument('--pocket_def_residues', type=str, default=None, help='Residues that you think would be close to the bound ligand for specifying the pocket in a format like this: "A60-65,A232,A233,A212-215,A325"')
    parser.add_argument('--pocket_def_center', type=str, default=None, help='String to define a pocket center like this: "-0.214,30.197,9.017"')

    # Training
    parser.add_argument('--batch_size', type=int, default=16, help='Batch size')
    parser.add_argument('--precision', type=str, default='medium', help='high, highest, medium')
    parser.add_argument('--gradient_clip_val', type=float, default=0.0, help='Gradient clipping value')
    parser.add_argument('--train_multiplicity', type=int, default=1, help='')
    parser.add_argument('--lr', type=float, default=1e-3, help='Initial learning rate')
    parser.add_argument('--warmup_dur', type=float, default=0)
    parser.add_argument('--constant_dur', type=float, default=5e9)
    parser.add_argument('--decay_dur', type=float, default=0)
    parser.add_argument('--lr_start', type=float, default=1)
    parser.add_argument('--lr_end', type=float, default=1)
    parser.add_argument('--epochs', type=int, default=50)
    parser.add_argument('--num_workers', type=int, default=4)
    parser.add_argument('--clamp_loss', type=float, default=None)
    parser.add_argument('--plateau_scheduler', action='store_true', default=False, help='')
    parser.add_argument('--fake_constant_dur', type=float, default=0, help='for how long to do fake ligand training with fake_ratio_start')
    parser.add_argument('--fake_decay_dur', type=float, default=0, help='for how long to decay fake ligand training from fake_ratio_start to fake_ratio_end')
    parser.add_argument('--fake_ratio_start', type=float, default=0)
    parser.add_argument('--fake_ratio_end', type=float, default=0)
    parser.add_argument('--l1_loss', action='store_true', default=False, help='')
    parser.add_argument('--pos_only_epochs', type=int, default=0, help='number of epochs in which the residue identity loss is set to 0')
    parser.add_argument('--num_angle_pred', type=int, default=0, help='how many angles to predict as auxiliary task. 5 corresponds to all side chain angles. 11 corresponds to also the backbone angles')
    parser.add_argument("--angle_loss_weight", type=float, default=0.2)
    parser.add_argument('--pos_loss_weight', type=float, default=0.01, help='weight for the coordinate loss compared to the residue decoding loss')
    parser.add_argument("--aux_weight", type=float, default=0.5)
    parser.add_argument("--residue_loss_weight", type=float, default=0.0)
    parser.add_argument('--num_pos_only_epochs', type=int, default=0, help='number of epochs in which the residue identity loss is set to 0')
    parser.add_argument('--num_all_res_train_epochs', type=int, default=1000000, help='for how many epochs to pretrain on the losses of all residues')
    parser.add_argument('--overfit_lig_idx', type=int, default=None, help='Overfit on the first complex and the ligand with this index')

    # General
    parser.add_argument('--checkpoint', type=str, default=None, help='A checkpoint to restart training from or to run inference from. ')
    parser.add_argument('--run_test', action='store_true', default=False, help='')
    parser.add_argument('--all_res_early_stop', action='store_true', default=False, help='use val_all_res_accuracy for early stopping instead of val_accuracy')
    parser.add_argument('--except_on_nan_grads', action='store_true', default=False, help='raise an exception if there are nan gradients')
    parser.add_argument('--ignore_lig', action='store_true', default=False, help='')

    # Flow Matching
    parser.add_argument('--flow_matching', action='store_true', default=False, help='Whether or not to use matching. Otherwise Diffusion is used.')
    parser.add_argument("--flow_matching_sigma", type=float, default=0.5)
    parser.add_argument("--velocity_prediction", action='store_true', default=False, help='')
    parser.add_argument("--prior_scale", type=float, default=1)
    parser.add_argument('--gaussian_prior', action='store_true', default=False, help='')
    parser.add_argument('--self_condition_inv', action='store_true', default=False, help='')
    parser.add_argument('--self_condition_x', action='store_true', default=False, help='Whether or not to use structure self conditioning')
    parser.add_argument('--self_condition_inv_logits', action='store_true', default=False, help='')
    parser.add_argument('--self_condition_bit', action='store_true', default=False, help='')
    parser.add_argument('--no_tfn_self_condition_inv', action='store_true', default=False, help='')
    parser.add_argument('--standard_style_self_condition_inv', action='store_true', default=False, help='')
    parser.add_argument('--self_fancy_init', action='store_true', default=False, help='')
    parser.add_argument("--self_condition_ratio", type=float, default=0.5, help='for what fraction of the forward passes to train with self conditioning')
    parser.add_argument('--num_integration_steps', type=int, default=20, help='The number of integration steps used during inference.')
    parser.add_argument('--time_conditioning', action='store_true', default=False, help='Wheter or not to condition the vectorfield / score model on time')
    parser.add_argument('--time_emb_dim', type=int, default=64, help='Embedding for the time variable')
    parser.add_argument('--time_emb_type', type=str, default='gaussian', help='[gaussian, sinusoidal, fourier] The type of embeddings used for the time variable. gaussian and fourier is basically the same.')
    parser.add_argument('--time_condition_inv', action='store_true', default=False, help='')
    parser.add_argument('--time_condition_tfn', action='store_true', default=False, help='')
    parser.add_argument('--time_condition_repeat', action='store_true', default=False, help='Whether to repeatedly insert the time embedding into the layers')

    # Diffusion
    parser.add_argument('--residue_diffusion', action='store_true', default=False, help='')
    parser.add_argument('--correct_time_condition', action='store_true', default=False, help='')
    parser.add_argument('--highest_noise_only', action='store_true', default=False, help='only train with time equal to 1. Num diffusion steps then should be 1 as well')
    parser.add_argument('--non_designable_extra_token', action='store_true', default=False, help='In the discrete diffusion the features are either masked with uniform probabilities from which to sample a feature, or if this is TRue, then with an extra special token')

    # Dataset
    parser.add_argument('--data_dir', type=str, default='data/PDBBind_processed/', help='Folder containing original structures')
    parser.add_argument('--train_split_path', type=str, default='index/test_indices', help='Path to the indices used for training')
    parser.add_argument('--val_split_path', type=str, default='index/test_indices', help='')
    parser.add_argument('--predict_split_path', type=str, default=None, help='')
    parser.add_argument('--data_source', type=str, default='pdbbind', help='[pdbbind, moad]')
    parser.add_argument('--data_source_combine', type=str, default=None, help='[pdbbind, moad]')
    parser.add_argument('--data_dir_combine', type=str, default=None, help='Folder containing original structures')
    parser.add_argument('--train_split_path_combine', type=str, default=None, help='Path to the indices used for training')
    parser.add_argument('--backbone_noise', type=float, default=0, help='')
    parser.add_argument('--biounit1_only', action='store_true', default=False, help='Only use Biounit1 for Binding MOAD')
    parser.add_argument('--lig_connection_radius', type=float, default=4.0, help='treat ligands with heavy atoms this close together as a single ligand. So this ligand will consist of multiple small molecules.')
    parser.add_argument('--cache_path', type=str, default='data/cache', help='Folder from where to load/restore cached dataset')
    parser.add_argument('--protein_file_name', type=str, default='protein_processed', help='')
    parser.add_argument('--protein_radius', type=float, default=15.0, help='')
    parser.add_argument('--ligand_edges', type=str, choices=['dense', 'radius'], default='radius')
    parser.add_argument('--lig_radius', type=float, default=15.0, help='')
    parser.add_argument('--cross_radius', type=float, default=20.0, help='')
    parser.add_argument('--max_lig_size', type=int, default=60)
    parser.add_argument('--min_lig_size', type=int, default=1)
    parser.add_argument('--use_true_pos', action='store_true', default=False)
    parser.add_argument('--mask_lig_pos', action='store_true', default=False, help='')
    parser.add_argument('--mask_lig_translation', action='store_true', default=False, help='')
    parser.add_argument('--mask_lig_rotation', action='store_true', default=False, help='')
    parser.add_argument('--lig_coord_noise', type=float, default=0.0, help='add gaussian noise to the ligand coordinates before each update layer')
    parser.add_argument('--num_chain_masks', type=int, default=7,help='When we train with fake ligand sidechains, we mask on each side of the residue in the chain. This is how much to mask on each side.')
    parser.add_argument('--min_chain_mask_dist', type=float, default=12, help='When doing the masking with num_chain_masks, we do not mask sidechains if they are farther away than this')
    parser.add_argument('--fake_min_num_contacts', type=int, default=4,help='minimum number of contacts necessary for a residue to be considered as a fake ligand sidechain')
    parser.add_argument('--min_num_contacts', type=int, default=1,help='minimum number of contacts necessary for a residue to be considered as a fake ligand sidechain')
    parser.add_argument('--delte_unreadable_cache', action='store_true', default=False, help='')
    parser.add_argument('--correct_moad_lig_selection', action='store_true', default=False, help='')
    parser.add_argument('--double_correct_moad_lig_selection', action='store_true', default=False, help='')
    parser.add_argument('--exclude_af2aa_excluded_ligs', action='store_true', default=False, help='')
    parser.add_argument('--dont_cache_dataset', action='store_true', default=False, help='does not store data in memory when using a dataset and instead always loads it from the files')
    parser.add_argument('--await_preprocessing', action='store_true', default=False, help='wait until the preprocessing is done by another process')
    parser.add_argument('--use_largest_lig', action='store_true', default=False, help='Option For binding moad to always use the largest ligand out of all of the ligands in the complex')
    parser.add_argument('--lm_embeddings', action='store_true', default=False, help='')

    # Pocket parameters
    parser.add_argument('--design_residue_cutoff', type=float, default=4, help='for the residues that should be predicted/generated')
    parser.add_argument('--pocket_residue_cutoff', type=float, default=None, help='for the residues that will be included as input to make the predictions')
    parser.add_argument('--pocket_type', type=str, choices=['distance', 'radius', 'diffdock', 'ca_distance', 'full_protein'], default='distance')
    parser.add_argument('--radius_pocket_buffer', type=float, default=10, help='Buffer that is added to the ligand radius when choosing the distance for including residues in the pocket')
    parser.add_argument('--pocket_residue_cutoff_sigma', type=float, default=0, help='Noise to add to minimum ligand distance for distance pockets')
    parser.add_argument('--pocket_center_sigma', type=float, default=0, help='Noise to add to the pocket center')

    ## Equivariant TFN refinement layers
    parser.add_argument('--use_tfn', action='store_true', default=False)
    parser.add_argument('--num_tfn_layers', type=int, default=6, help='Number of interaction layers')
    parser.add_argument('--ns', type=int, default=32, help='Number of hidden features per node of order 0')
    parser.add_argument('--nv', type=int, default=8, help='Number of hidden features per node of order >0. Must at least be 3')
    parser.add_argument("--fc_dim", type=int, default=128)
    parser.add_argument('--radius_emb_dim', type=int, default=64, help='Embedding size for the distance')
    parser.add_argument("--batch_norm", action="store_true")
    parser.add_argument('--sh_lmax', type=int, default=1, help='')
    parser.add_argument("--order", type=int, default=1)
    parser.add_argument("--layer_norm", action="store_true")
    parser.add_argument("--feedforward", action="store_true")
    parser.add_argument("--pre_norm", action="store_true")
    parser.add_argument("--post_norm", action="store_true")
    parser.add_argument("--fancy_init", action="store_true")
    parser.add_argument("--no_damping_factor", action="store_true")
    parser.add_argument("--separate_update", action="store_true")
    parser.add_argument("--fixed_lig_pos", action="store_true")
    parser.add_argument("--update_last_when_fixed", action="store_true")
    parser.add_argument('--tfn_use_aa_identities', action='store_true', default=False, help='Use AA identities as input for the TFN layers')
    parser.add_argument("--tfn_pifold_feat", action="store_true", help='Use the invariant features of PiFold as additional input to the Tensor Field Network')
    parser.add_argument("--faster", action="store_true", help='Use the faster TFN layers')
    parser.add_argument("--no_tfn_rec2rec", action="store_true", help='Do not pass messages from the receptor to the receptor in the TFN layers')
    parser.add_argument("--residual", action="store_true")
    parser.add_argument('--no_tfn_vector_inputs', action='store_true', default=False, help='')
    parser.add_argument('--tfn_detach', action='store_true', default=False, help='')
    parser.add_argument('--tfn_straight_combine', action='store_true', default=False)

    ## Invariant layers
    parser.add_argument('--use_inv', action='store_true', default=False)
    parser.add_argument("--no_inv_layers", action="store_true")
    parser.add_argument('--fold_dim', default=128, type=int)
    parser.add_argument('--k_neighbors', default=30, type=int)
    parser.add_argument('--inv_dropout', default=0.1, type=float)
    parser.add_argument('--num_inv_layers', default=10, type=int)
    parser.add_argument('--updating_edges', default=4, type=int)
    parser.add_argument('--node_dist', default=1, type=int)
    parser.add_argument('--node_angle', default=1, type=int)
    parser.add_argument('--node_direct', default=1, type=int)
    parser.add_argument('--edge_dist', default=1, type=int)
    parser.add_argument('--edge_angle', default=1, type=int)
    parser.add_argument('--edge_direct', default=1, type=int)
    parser.add_argument('--virtual_num', default=3, type=int)
    parser.add_argument('--edge_context', action='store_true', default=False)
    parser.add_argument('--node_context', action='store_true', default=False)
    parser.add_argument('--drop_tfn_feat', action='store_true', default=False)
    parser.add_argument('--inv_straight_combine', action='store_true', default=False)

    # Optional additional initial MPNN embeddings for the ligand
    parser.add_argument('--lig2d_mpnn', action='store_true', default=False, help='')
    parser.add_argument('--lig2d_batch_norm', action='store_true', default=False, help='')
    parser.add_argument('--lig2d_additional_relu', action='store_true', default=False, help='')
    parser.add_argument('--lig_mpnn_dim', type=int, default=64, help='This is no longer used in the new ResPosModel architecture')
    parser.add_argument('--lig_mpnn_layers', type=int, default=0, help='')


    # Optional parameters for CS 236 Extension
    parser.add_argument('--sidechain_with_ligand', action='store_true', default=False, help='')
    parser.add_argument('--sidechain_alternate', action='store_true', default=False, help='')

    args = parser.parse_args(args)
    return args
