import __init__
#
from community_analysis import ft_trips_dir, ft_trips_prefix
from community_analysis import dw_graph_dir, dw_graph_prefix, dw_graph_above_avg_prefix
from community_analysis import dw_year_summary_fpath
#
from taxi_common.file_handling_functions import load_pickle_file, check_path_exist, save_pickle_file
from taxi_common.log_handling_functions import get_logger
#
import numpy as np
import csv
#
logger = get_logger('year')


def run():
    if not check_path_exist(dw_year_summary_fpath):
        with open(dw_year_summary_fpath, 'wt') as w_csvfile:
            writer = csv.writer(w_csvfile, lineterminator='\n')
            writer.writerow(['year', 'days','numDrivers',
                                'numPickupsTotal', 'numPickupsAverage', 'numPickupsSD',
                                'numPickupsMedian', 'numPickupsMin', 'numPickupsMax',
                             'numLinks',
                                'weightTotal', 'weightAverage', 'weightSD',
                                'weightMedian', 'weightMin', 'weightMax'])
    for y in range(11, 13):
        yyyy = '20%02d' % y
        logger.info('Handle %s' % yyyy)
        driver_pickup = {}
        year_dw_graph = {}
        for m in range(1, 13):
            yymm = '%02d%02d' % (y, m)
            logger.info('Loading %s' % yymm)
            month_dw_graph_fpath = '%s/%s%s.pkl' % (dw_graph_dir, dw_graph_prefix, yymm)
            if not check_path_exist(month_dw_graph_fpath):
                continue
            month_dw_graph = load_pickle_file(month_dw_graph_fpath)
            for did0, num_pickup, weighted_link in month_dw_graph:
                if not driver_pickup.has_key(did0):
                    driver_pickup[did0] = 0
                driver_pickup[did0] += num_pickup
                #
                for did1, weight in weighted_link.iteritems():
                    k = (did0, did1)
                    if not year_dw_graph.has_key(k):
                        year_dw_graph[k] = 0.0
                    year_dw_graph[k] += weight
            logger.info('Finish %s' % yymm)
        logger.info('Saving year_dw_graph0 %s' % yyyy)
        year_dw_graph0_fpath = '%s/%s%s.pkl' % (dw_graph_dir, dw_graph_prefix, yyyy)
        save_pickle_file(year_dw_graph0_fpath, year_dw_graph)
        #
        logger.info('Saving year_dw_graph1 %s' % yyyy)
        year_dw_graph1_fpath = '%s/%s%s.pkl' % (dw_graph_dir, dw_graph_above_avg_prefix, yyyy)
        weight_avg = np.asarray(year_dw_graph.values()).mean()
        year_dw_graph_above_avg = {k: v for k, v in year_dw_graph.iteritems() if v > weight_avg}
        save_pickle_file(year_dw_graph1_fpath, year_dw_graph_above_avg)
        #
        logger.info('Generate summary statistics %s' % yyyy)
        num_drivers = len(driver_pickup)
        num_links = len(year_dw_graph)
        pickups, weights = np.asarray(driver_pickup.values()), np.asarray(year_dw_graph.values())
        month_day = set()
        for m in range(1, 12):
            yymm = '%02d%02d' % (y, m)
            ft_trips_fpath = '%s/%s%s.csv' % (ft_trips_dir, ft_trips_prefix, yymm)
            with open(ft_trips_fpath, 'rb') as r_csvfile:
                reader = csv.reader(r_csvfile)
                headers = reader.next()
                hid = {h: i for i, h in enumerate(headers)}
                for row in reader:
                    day = row[hid['day']]
                    month_day.add((m, day))
        with open(dw_year_summary_fpath, 'a') as w_csvfile:
            writer = csv.writer(w_csvfile, lineterminator='\n')
            writer.writerow([yyyy, len(month_day), num_drivers,
                                pickups.sum(), pickups.mean(), pickups.std(),
                                np.median(pickups), pickups.min(), pickups.max(),
                             num_links,
                                weights.sum(), weights.mean(), weights.std(),
                                np.median(weights), weights.min(), weights.max()])



if __name__ == '__main__':
    run()