import __init__
#
'''

'''
#
from community_analysis import SP_graph_dpath, SP_graph_prefix
from community_analysis import RP_graph_dpath, RP_graph_prefix
from community_analysis import SP_group_dpath, SP_group_prefix
from community_analysis import SP_group_drivers_fpath
from community_analysis import SP_group_summary_fpath
from community_analysis import RP_group_dpath, RP_group_prefix
from community_analysis import RP_group_drivers_fpath
from community_analysis import RP_group_summary_fpath
#
from taxi_common.file_handling_functions import check_dir_create, get_all_files, load_pickle_file, save_pickle_file
from taxi_common.log_handling_functions import get_logger
#
import csv
import louvain
import igraph as ig

logger = get_logger()


def run():
    for graph_dpath, graph_prefix, group_dpath, group_prefix, group_drivers_fapth, group_summary_fpath in \
        [
         (SP_graph_dpath, SP_graph_prefix, SP_group_dpath, SP_group_prefix, SP_group_drivers_fpath, SP_group_summary_fpath),
         # (RP_graph_dpath, RP_graph_prefix, RP_group_dpath, RP_group_prefix, RP_group_drivers_fpath, RP_group_summary_fpath)
        ]:
        check_dir_create(group_dpath)
        with open(group_summary_fpath, 'wt') as w_csvfile:
            writer = csv.writer(w_csvfile, lineterminator='\n')
            writer.writerow(['groupName', 'numDrivers', 'tieStrength'])
        #
        logger.info('Start handling SP_group_dpath')
        igid, did_igid = 0, {}
        igG = ig.Graph(directed=True)
        for fn in get_all_files(graph_dpath, '%s*' % graph_prefix):
            regression_graph = load_pickle_file('%s/%s' % (graph_dpath, fn))
            num_edges = len(regression_graph)
            cur_percent = 0
            for i, ((did0, did1), w) in enumerate(regression_graph.iteritems()):
                per = (i / float(num_edges))
                if per * 100 > cur_percent:
                    cur_percent += 1
                    logger.info('processed %.2f edges (%s)' % (i / float(num_edges), fn))
                if not did_igid.has_key(did0):
                    igG.add_vertex(did0)
                    did_igid[did0] = igid
                    igid += 1
                if not did_igid.has_key(did1):
                    igG.add_vertex(did1)
                    did_igid[did1] = igid
                    igid += 1
                igG.add_edge(did_igid[did0], did_igid[did1], weight=abs(w))
        logger.info('Partitioning')
        part = louvain.find_partition(igG, method='Modularity', weight='weight')
        #
        logger.info('Each group pickling and summary')
        group_drivers = {}
        for i, sg in enumerate(part.subgraphs()):
            gn = 'G(%d)' % i
            group_fpath = '%s/%s%s.pkl' % (group_dpath, group_prefix, gn)
            sg.write_pickle(group_fpath)
            #
            drivers = [v['name'] for v in sg.vs]
            weights = [e['weight'] for e in sg.es]
            with open(group_summary_fpath, 'a') as w_csvfile:
                writer = csv.writer(w_csvfile, lineterminator='\n')
                writer.writerow([gn, len(drivers), sum(weights) / float(len(drivers))])
            group_drivers[gn] = drivers
        save_pickle_file(group_drivers_fapth, group_drivers)


if __name__ == '__main__':
    run()

