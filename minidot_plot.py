import os
import numpy as np
import matplotlib.pyplot as plt
from minidot_concat import concat_minidot
from config import System


def minidot_plot():
    """------------------------------------------------------------
    FUNCTION Plot the measurements from the 4 sensors installed at
    the Passaúna reservoir, at the metropolitan region of Curitiba,
    in the south of Brazil. Each sensor measures dissolved oxygen 
    and water temperature.
    ---------------------------------------------------------------
    RETURN SVG PNG and JPEG files
    ------------------------------------------------------------"""

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))
    ax_index = {'fundo': 0, 'sup': 1}
    ax_title = {'fundo': 'bottom', 'sup': 'surface'}
    colors = {'pv1': 'r', 'lr': 'b'}

    minidot_dict = concat_minidot()

    for folder in os.listdir(System.DATAPATH):

        folder_split = folder.split('_')
        site = folder_split[0]
        depth = folder_split[1]
        ax_col = ax_index[depth]
        title = f'LR x PV1 ({ax_title[depth]})'
        do_col = f'DO (mg/l) {site.upper()}'
        t_col = f'T (°C) {site.upper()}'
        do_y_ticks = np.arange(0, 16, 2)
        t_y_ticks = np.arange(15, 35, 2)
        rename_dict = {
            '  DO (mg/l)': do_col,
            '  T (deg C)': t_col
            }

        df = minidot_dict[folder].rename(columns=rename_dict)

        df[do_col].plot(ax=axes[0, ax_col],
                        legend=True,
                        title=title,
                        ylabel='mg/l',
                        fontsize=11,
                        color=colors[site],
                        linewidth=1.0,
                        yticks=do_y_ticks)
        df[t_col].plot(ax=axes[1, ax_col],
                       legend=True,
                       ylabel='°C',
                       fontsize=11,
                       xlabel='Date',
                       color=colors[site],
                       linewidth=1.0,
                       yticks=t_y_ticks)

        axes[0, 1].yaxis.set_ticklabels([])
        axes[1, 1].yaxis.set_ticklabels([])
        axes[0, 1].yaxis.label.set_visible(False)
        axes[1, 1].yaxis.label.set_visible(False)

        axes[0, 0].xaxis.set_ticklabels([])
        axes[0, 1].xaxis.set_ticklabels([])
        axes[0, 0].xaxis.label.set_visible(False)
        axes[0, 1].xaxis.label.set_visible(False)

    f_types = ['.svg', '.png', '.jpg']
    for f_type in f_types: 
        figname = f'{System.GRAPH_PATH}/minidot_oct-22_fev-23{f_type}'
        plt.savefig(figname, dpi=600)
    
    plt.tight_layout()
    plt.show()
 

if __name__ == "__main__":

    minidot_plot()