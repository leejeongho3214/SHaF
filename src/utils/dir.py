import json
import os
import shutil
import sys

import torch


def dump(pred_out_path, xyz_pred_list):
    """Write the predictions to a json file."""
    with open(pred_out_path, "w") as f:
        json.dump([xyz_pred_list], f)


def reset_file(path):
    """Delete a file if it exists."""
    if os.path.isfile(path):
        os.remove(path)


def reset_folder(path):
    """Create an empty folder, removing any previous contents."""
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.makedirs(path)


def add_pypath(path):
    if path not in sys.path:
        sys.path.insert(0, path)


def resume_checkpoint(_model, path):
    state_dict = torch.load(path, map_location="cpu", weights_only=False)
    best_loss = state_dict["best_loss"]
    epoch = state_dict["epoch"] + 1
    count = state_dict["count"]
    missing, unexpected = _model.load_state_dict(state_dict["model_state_dict"], strict=False)
    if missing or unexpected:
        print("[resume_checkpoint] WARNING: checkpoint does not match the current "
              "architecture flags (%d missing, %d unexpected keys). Check --backbone/"
              "--which_gcn/--graph_num/--num_hidden_layers or use --reset."
              % (len(missing), len(unexpected)))
    del state_dict

    return best_loss, epoch, _model, count
