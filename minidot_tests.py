import pandas as pd
from config import System
from minidot_concat import concat_minidot
from statistical_tests import mwhitney_test


def minidots_mwhitney():
    """--------------------------------------------------------------
    FUNCTION This function tests if there are significant differences
    among the measurements of water temperature and dissolved oxygen
    from 4 distinct sensors (miniDOTs).
    -----------------------------------------------------------------
    METHOD  Mann-Whitney Test (Sheskin, 2004) - Non parametric
    -----------------------------------------------------------------
    CONTEXT In the project FotoAgua these sensors are set in the 
    Passaúna Reservoir, in the metropolitan region of Curitiba, in 
    the south of Brazil. There are 2 sensors installed underneath a 
    floating photovoltaic power plant (1 at the surface and 1 at the 
    bottom), and another 2 sensors installed at a reference point at 
    the reservoir, also bottom and surface. The objective is evaluate
    the impact from the photovoltaic system on water quality, due to 
    shading.
    -----------------------------------------------------------------
    RESULT .csv file with the results of the test for each parameter
    
    Example:
    -----------------------------------------------------------------
    HYPOTHESIS SURFACE                   BOTTOM
    -----------------------------------------------------------------
    LR = PV1   (stat:70, p-value:0.005)  (stat:-40.5, p-value:0.000)
    LR > PV1   True                      False
    LR < PV1   False                     True
    -----------------------------------------------------------------
    LR = reference point, away from photovoltaic system
    PV1 = point underneath the photovoltaic system
    --------------------------------------------------------------"""
    
    folders = ['lr_fundo', 'lr_sup', 'pv1_fundo', 'pv1_sup']
    cols = ['  DO (mg/l)', '  T (deg C)']

    minidot_dict = concat_minidot()

    do_lr_bottom = minidot_dict[folders[0]][cols[0]].values.tolist()
    do_pv1_bottom = minidot_dict[folders[2]][cols[0]].values.tolist()
    do_lr_surf = minidot_dict[folders[1]][cols[0]].values.tolist()
    do_pv1_surf = minidot_dict[folders[3]][cols[0]].values.tolist()
    
    do_dict = {
        'b': [do_lr_bottom, do_pv1_bottom],
        's': [do_lr_surf, do_pv1_surf],
        'fname': 'do'
        }
    
    t_lr_bottom = minidot_dict[folders[0]][cols[1]].values.tolist()
    t_pv1_bottom = minidot_dict[folders[2]][cols[1]].values.tolist()
    t_lr_surf = minidot_dict[folders[1]][cols[1]].values.tolist()
    t_pv1_surf = minidot_dict[folders[3]][cols[1]].values.tolist()
    
    t_dict = {
        'b': [t_lr_bottom, t_pv1_bottom],
        's': [t_lr_surf, t_pv1_surf],
        'fname': 't'
        }

    all_data = [do_dict, t_dict]

    for data in all_data:

        s_test = mwhitney_test({'LR_SURF': data['s'][0], 'PV1_SURF': data['s'][1]})
        b_test = mwhitney_test({'LR_BOTTOM': data['b'][0], 'PV1_BOTTOM': data['b'][1]})

        decision_s = s_test['decision']
        stats_s = s_test['stats']
        decision_b = b_test['decision']
        stats_b = b_test['stats']

        try:
            df_dict = {
                'Hypotheses': ['LR = PV1', 'LR > PV1', 'LR < PV1'],
                'Surface': [
                    f"{decision_s['H0: PV1_SURF == LR_SURF']} (stat: {stats_s[0]}, p-valor: {stats_s[1]})",
                    decision_s['H1: PV1_SURF < LR_SURF'],
                    decision_s['H2: PV1_SURF > LR_SURF'],
                    ],
                'Bottom': [
                    f"{decision_b['H0: LR_BOTTOM == PV1_BOTTOM']} (stat: {stats_b[0]}, p-valor: {stats_b[1]})",
                    decision_b['H1: LR_BOTTOM < PV1_BOTTOM'],
                    decision_b['H2: LR_BOTTOM > PV1_BOTTOM'],
                    ],
                }

        except KeyError:
            df_dict = {
                'Hypotheses': ['LR = PV1', 'LR > PV1', 'LR < PV1'],
                'Surface': [
                    f"{decision_s['H0: PV1_SURF == LR_SURF']} (stat: {stats_s[0]}, p-valor: {stats_s[1]})",
                    decision_s['H1: PV1_SURF < LR_SURF'],
                    decision_s['H2: PV1_SURF > LR_SURF'],
                    ],
                'Bottom': [
                    f"{decision_b['H0: PV1_BOTTOM == LR_BOTTOM']} (stat: {stats_b[0]}, p-valor: {stats_b[1]})",
                    decision_b['H1: PV1_BOTTOM < LR_BOTTOM'],
                    decision_b['H2: PV1_BOTTOM > LR_BOTTOM'],
                    ],
                }

        df = pd.DataFrame(df_dict)
        df.to_csv(f"{System.STATSPATH}/{data['fname']}_stats.csv")


if __name__ == "__main__":

    minidots_mwhitney()