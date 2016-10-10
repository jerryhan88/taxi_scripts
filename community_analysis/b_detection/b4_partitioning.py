import __init__
#
from community_analysis import dw_graph_dir, dw_graph_above_avg_prefix, dw_graph_above_per90_prefix, dw_graph_above_per95_prefix
from community_analysis import group_dir, group_prepix
#
from taxi_common.file_handling_functions import load_pickle_file, check_path_exist, check_dir_create
from taxi_common.log_handling_functions import get_logger
#
import louvain
import igraph as ig

logger = get_logger('partitioning_month3_99')


def run():
    check_dir_create(group_dir)

    month3_dw_graph_fn = 'dw-graph-above-per99-2009-M01M02M03.pkl'
    # month3_dw_graph_fn = 'dw-graph-above-per99-2009-M02M03M04.pkl'
    month3_dw_graph_fpath = '%s/%s' % (dw_graph_dir, month3_dw_graph_fn)
    #
    _, _, _, per, yyyy, month3 = month3_dw_graph_fn[:-len('.pkl')].split('-')


    logger.info('month3 dw graph loading')
    month3_dw_graph_above_per99 = load_pickle_file(month3_dw_graph_fpath)
    num_edges = len(month3_dw_graph_above_per99)
    logger.info('igraph generation total number of edges %d' % num_edges)
    igid, did_igid = 0, {}
    igG = ig.Graph(directed=True)
    for i, ((did0, did1), w) in enumerate(month3_dw_graph_above_per99.iteritems()):
    #
    # yyyy = '2009'
    # #
    # # year_group_fpath = '%s/%s%s.pkl' % (group_dir, group_prepix, yyyy)
    # # if check_path_exist(year_group_fpath):
    # #     return None
    # # logger.info('year dw graph loading')
    # # year_dw_graph1_fpath = '%s/%s%s.pkl' % (dw_graph_dir, dw_graph_above_per95_prefix, yyyy)
    # # year_dw_graph_above_avg = load_pickle_file(year_dw_graph1_fpath)
    # # num_edges = len(year_dw_graph_above_avg)
    # # logger.info('igraph generation total number of edges %d' % num_edges)
    # # igid, did_igid = 0, {}
    # # igG = ig.Graph(directed=True)
    # # for i, ((did0, did1), w) in enumerate(year_dw_graph_above_avg.iteritems()):
        if i % 5000 == 0:
            logger.info('processed %.3f edges' % (i / float(num_edges)))
        if not did_igid.has_key(did0):
            igG.add_vertex(did0)
            did_igid[did0] = igid
            igid += 1
        if not did_igid.has_key(did1):
            igG.add_vertex(did1)
            did_igid[did1] = igid
            igid += 1
        igG.add_edge(did_igid[did0], did_igid[did1], weight=w)
    logger.info('Partitioning')
    part = louvain.find_partition(igG, method='Modularity', weight='weight')
    logger.info('Whole group pickling')
    month3_group_fpath = '%s/%s%s-%s-%s.pkl' % (group_dir, group_prepix, per, yyyy, month3)
    part.graph.write_pickle(month3_group_fpath)
    logger.info('Each group pickling')
    for i, sg in enumerate(part.subgraphs()):
        month3_a_group_fpath = '%s/%s%s-%s-%s-G(%d).pkl' % (group_dir, group_prepix, per, yyyy, month3, i)
        sg.write_pickle(month3_a_group_fpath)


if __name__ == '__main__':
    run()