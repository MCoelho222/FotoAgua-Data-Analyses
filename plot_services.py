import numpy as np


def nrows_ncols_for_subplots(dfs_dict):
    """----------------------------------------------
    FUNCTION Defines the number of rows and cols for
    pyplot subplots figure
    -------------------------------------------------
    PARAMETER
    dfs_dict => the dict that has each subplot content
    in its keys
    --------------------------------------------------
    RETURN tuple => (rows: int64, cols: int64)
    -----------------------------------------------"""
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

