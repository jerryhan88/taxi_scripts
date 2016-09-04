import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
#
from taxi_common.__init__ import get_taxi_home_path
taxi_home = get_taxi_home_path()
#
from taxi_common.file_handling_functions import check_dir_create
taxi_data = os.path.dirname(os.path.realpath(__file__)) + '/data'; check_dir_create(taxi_data)
#
trip_dir = '%s/%s' % (taxi_data, 'trips')
ld_dir = '%s/%s' % (taxi_data, 'linkage_daily')
lm_dir = '%s/%s' % (taxi_data, 'linkage_monthly')
la_dir = '%s/%s' % (taxi_data, 'linkage_annually')
com_dir = '%s/%s' % (taxi_data, 'community')
com_trip_dir = '%s/%s' % (taxi_data, 'com_trips')


# pg_dir = taxi_data + '/partitioned_group'; check_dir_create(pg_dir)
#
# com_trip_dir = taxi_data + '/ctrips'; check_dir_create(com_trip_dir)
#
# com_log_dir = taxi_data + '/com_logs'; check_dir_create(com_log_dir)
# com_linkage_dir = taxi_data + '/com_linkage'; check_dir_create(com_linkage_dir)
# cevol_dir = taxi_data + '/cevol'; check_dir_create(cevol_dir)

#
MON, TUE, WED, THR, FRI, SAT, SUN = range(7)
PM2, PM3 = 14, 15
PM11 = 23