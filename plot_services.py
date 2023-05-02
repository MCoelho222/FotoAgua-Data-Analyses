import numpy as np


def nrows_ncols_for_subplots(dfs_dict):

    keys = list(dfs_dict.keys())
    s = len(keys)

    if s < 29:
        div = 4
    if s == 25:
        div = 5
    if s < 16:
        div = 3
    if s < 9:
        div = 2

    nrows = int(np.ceil(len(keys)/div))
    ncols = div

    return (nrows, ncols)

