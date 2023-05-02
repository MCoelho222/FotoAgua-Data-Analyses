from os.path import dirname, abspath, join
import pandas as pd
from minidot_concat import concat_minidot
from statistical_tests import mwhitney_test


ROOTPATH = dirname(abspath(__file__))
DATAPATH = join(ROOTPATH, 'minidot_data')
STATSPATH = join(ROOTPATH, 'minidot_stats')


def minidot_mwhitney():

    folders = ['lr_fundo', 'lr_sup', 'pv1_fundo', 'pv1_sup']
    cols = ['  DO (mg/l)', '  T (deg C)']

    minidot_dict = concat_minidot()

    do_lr_bottom = minidot_dict[folders[0]][cols[0]].values.tolist()
    t_lr_bottom = minidot_dict[folders[0]][cols[1]].values.tolist()
    do_pv1_bottom = minidot_dict[folders[2]][cols[0]].values.tolist()
    t_pv1_bottom = minidot_dict[folders[2]][cols[1]].values.tolist()

    do_lr_surf = minidot_dict[folders[1]][cols[0]].values.tolist()
    t_lr_surf = minidot_dict[folders[1]][cols[1]].values.tolist()
    do_pv1_surf = minidot_dict[folders[3]][cols[0]].values.tolist()
    t_pv1_surf = minidot_dict[folders[3]][cols[1]].values.tolist()

    do_bottom_test = mwhitney_test({'LR_BOTTOM': do_lr_bottom, 'PV1_BOTTOM': do_pv1_bottom})
    do_surf_test = mwhitney_test({'LR_SURF': do_lr_surf, 'PV1_SURF': do_pv1_surf})
    t_bottom_test = mwhitney_test({'LR_BOTTOM': t_lr_bottom, 'PV1_BOTTOM': t_pv1_bottom})
    t_surf_test = mwhitney_test({'LR_SURF': t_lr_surf, 'PV1_SURF': t_pv1_surf})

    do_df_dict = {
        'Hipótese': ['LR = PV1', 'LR > PV1', 'LR < PV1'],
        'Superfície': [f"{do_surf_test['decision']['H0: PV1_SURF == LR_SURF']} (stat: {do_surf_test['stats'][0]}, p-valor: {do_surf_test['stats'][1]})",
                  do_surf_test['decision']['H1: PV1_SURF < LR_SURF'],
                  do_surf_test['decision']['H2: PV1_SURF > LR_SURF']
                  ],
        'Fundo': [f"{do_bottom_test['decision']['H0: LR_BOTTOM == PV1_BOTTOM']} (stat: {do_bottom_test['stats'][0]}, p-valor: {do_bottom_test['stats'][1]})",
                  do_bottom_test['decision']['H2: LR_BOTTOM > PV1_BOTTOM'],
                  do_bottom_test['decision']['H1: LR_BOTTOM < PV1_BOTTOM']
                  ]
        }

    t_df_dict = {
        'Hipótese': ['LR = PV1', 'LR > PV1', 'LR < PV1'],
        'Superfície': [f"{t_surf_test['decision']['H0: PV1_SURF == LR_SURF']} (stat: {t_surf_test['stats'][0]}, p-valor: {t_surf_test['stats'][1]})",
                  t_surf_test['decision']['H1: PV1_SURF < LR_SURF'],
                  t_surf_test['decision']['H2: PV1_SURF > LR_SURF']
                  ],
        'Fundo': [f"{t_bottom_test['decision']['H0: LR_BOTTOM == PV1_BOTTOM']} (stat: {t_bottom_test['stats'][0]}, p-valor: {t_bottom_test['stats'][1]})",
                  t_bottom_test['decision']['H2: LR_BOTTOM > PV1_BOTTOM'],
                  t_bottom_test['decision']['H1: LR_BOTTOM < PV1_BOTTOM']
                  ]
        }
    
    do_df = pd.DataFrame(do_df_dict)
    t_df = pd.DataFrame(t_df_dict)
    do_df.to_excel(f'{STATSPATH}/do_stats.xlsx')
    t_df.to_excel(f'{STATSPATH}/t_stats.xlsx')
    
    return

if __name__ == "__main__":

    minidot_mwhitney()