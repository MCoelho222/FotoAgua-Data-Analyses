import os
import pandas as pd
import numpy as np
from config import System

col_names = ['Time (sec)', 'BV (Volts)', 'T (deg C)', 'DO (mg/l)', 'Q ()']


def concat_minidot(save=False):
    """--------------------------------------------------------------
    FUNCTION Concatenates the daily CSV files from miniDOT sensors,
    into a unique CSV, which will have all the measurements of a
    sensor. As there are 4 sensors available at the time, the files
    from each one must be in the correspondent sub-folders of the 
    minidot_data folder, according to their location in the reservoir.
    ------------------------------------------------------------------
    RETURN a dict with 4 dataframes; a CSV file for each sensor saved
    in the minidot_concat folder.
    ---------------------------------------------------------------"""

    minidot_dict = {}
    for folder in os.listdir(System.DATAPATH):
        minidot_df = pd.DataFrame(columns=col_names)
        minidot_df = minidot_df.set_index('Time (sec)')
        MINIDOT_PATH = os.path.join(System.DATAPATH, folder)

        for f in os.listdir(MINIDOT_PATH):
            FILE_PATH = os.path.join(MINIDOT_PATH, f)
            df = pd.read_csv(FILE_PATH, skiprows=2, index_col=0)
            df.index = pd.to_datetime(df.index, unit='s') - pd.Timedelta(hours=3)

            # This is a correction due to a problem in dec2022-jan2023
            if folder == 'pv1_sup':
                start_check = np.datetime64('2022-12-26')
                end_check = np.datetime64('2023-01-16')
                err_date = np.datetime64(f.split(' ')[0])
                if err_date >= start_check and err_date <= end_check:
                    df.index += pd.Timedelta(days=31)

            minidot_df =  pd.concat([minidot_df, df], axis=0)
            minidot_df = minidot_df.dropna(axis=1, how='all')

        minidot_df.index = minidot_df.index.rename('Datetime (local)')

        if save:
            SAVE_FILE_PATH = os.path.join(System.CONCAT_DATAPATH, folder + '.csv')
            minidot_df.to_csv(f'{SAVE_FILE_PATH}')
        minidot_dict[folder] = minidot_df

    return minidot_dict


if __name__ == "__main__":

    concat_minidot(save=True)