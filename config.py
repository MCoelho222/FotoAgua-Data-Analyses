from os.path import dirname, abspath, join

class System:

    ROOTPATH = dirname(abspath(__file__))
    DATAPATH = join(ROOTPATH, 'minidot_data')
    CONCAT_DATAPATH = join(ROOTPATH, 'minidot_concat')
    GRAPH_PATH = join(ROOTPATH, 'minidot_graphs')
    STATSPATH = join(ROOTPATH, 'minidot_stats')