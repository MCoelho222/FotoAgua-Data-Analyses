import os
from os.path import dirname, abspath, join
import numpy as np
import matplotlib.pyplot as plt
from minidot_concat import concat_minidot


ROOTPATH = dirname(abspath(__file__))
DATAPATH = join(ROOTPATH, 'minidot_data')
GRAPH_PATH = join(ROOTPATH, 'minidot_graphs')


def minidot_plot():

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8))
    ax_index = {'fundo': 0, 'sup': 1}
    ax_title = {'fundo': 'bottom', 'sup': 'surface'}
    colors = {'pv1': 'r', 'lr': 'b'}

    minidot_dict = concat_minidot()

    for folder in os.listdir(DATAPATH):

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

        df = minidot_dict[folder].rename(columns = rename_dict)

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
        axes[0, 1].xaxis.set_ticklabels([])
        axes[0, 0].xaxis.set_ticklabels([])
        axes[0, 0].xaxis.label.set_visible(False)
        axes[0, 1].xaxis.label.set_visible(False)
        axes[0, 1].yaxis.label.set_visible(False)
        axes[1, 1].yaxis.label.set_visible(False)

    figname1 = f'{GRAPH_PATH}/minidot_oct-22_fev-23.svg'
    figname2 = f'{GRAPH_PATH}/minidot_oct-22_fev-23.png'
    figname3 = f'{GRAPH_PATH}/minidot_oct-22_fev-23.jpg'
    plt.tight_layout()
    plt.savefig(figname1)
    plt.savefig(figname2, dpi=600)
    plt.savefig(figname3, dpi=600)
    plt.show()
 
    return

if __name__ == "__main__":

    minidot_plot()