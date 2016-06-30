from __future__ import division
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../..')
import information_boards.__init__
#
# full time drivers data
#
from __init__ import taxi_data, summary_dir
check_dir_create(taxi_data)
check_dir_create(summary_dir)
#
full_time_drivers_dir = taxi_data + '/full_time_driver'
ftd_trips_dir, ftd_trips_prefix = full_time_drivers_dir + '/ftd_trips', 'ftd-trips-'
ftd_shift_dir, ftd_shift_prefix = full_time_drivers_dir + '/ftd_shift', 'ftd-shift-'
ftd_list_dir, ftd_list_prefix =  full_time_drivers_dir + '/ftd_list', 'ftd-list-'
ftd_gen_stat_dir, ftd_gen_stat_prefix = full_time_drivers_dir + '/ftd_gen_stat', 'ftd-gen-stat-'
ftd_prev_in_ap_stat_dir, ftd_prev_in_ap_stat_prefix = full_time_drivers_dir + '/ftd_prev_in_ap_stat', 'ftd-prev-in-ap-stat-'
ftd_prev_in_ns_stat_dir, ftd_prev_in_ns_stat_prefix = full_time_drivers_dir + '/ftd_prev_in_ns_stat', 'ftd-prev-in-ns-stat-'
ftd_prev_out_ap_stat_dir, ftd_prev_out_ap_stat_prefix = full_time_drivers_dir + '/ftd_prev_out_ap_stat', 'ftd-prev-out-ap-stat-'
ftd_prev_out_ns_stat_dir, ftd_prev_out_ns_stat_prefix = full_time_drivers_dir + '/ftd_prev_out_ns_stat', 'ftd-prev-out-ns-stat-'
#
Y09_ftd_gen_stat = summary_dir + '/Y09-ftd-gen-stat.csv'
Y10_ftd_gen_stat = summary_dir + '/Y10-ftd-gen-stat.csv'
Y09_ftd_prev_in_ap_stat = summary_dir + '/Y09-ftd-prev-in-ap-stat.csv'
Y10_ftd_prev_in_ap_stat = summary_dir + '/Y10-ftd-prev-in-ap-stat.csv'
Y09_ftd_prev_in_ns_stat = summary_dir + '/Y09-ftd-prev-in-ns-stat.csv'
Y10_ftd_prev_in_ns_stat = summary_dir + '/Y10-ftd-prev-in-ns-stat.csv'
Y09_ftd_prev_out_ap_stat = summary_dir + '/Y09-ftd-prev-out-ap-stat.csv'
Y10_ftd_prev_out_ap_stat = summary_dir + '/Y10-ftd-prev-out-ap-stat.csv'
Y09_ftd_prev_out_ns_stat = summary_dir + '/Y09-ftd-prev-out-ns-stat.csv'
Y10_ftd_prev_out_ns_stat = summary_dir + '/Y10-ftd-prev-out-ns-stat.csv'
#
ftd_gen_prod_mb = summary_dir + '/ftd-gen-prod-month-based.pkl'
ftd_ap_prod_eco_prof_mb = summary_dir + '/ftd-ap-prod-eco-prof-month-based.pkl'
ftd_ns_prod_eco_prof_mb =summary_dir + '/ftd-ns-prod-eco-prof-month-based.pkl'
#
ftd_gen_prod_db_for_ap = summary_dir + '/ftd-gen-prod-drivers-based-for-ap.pkl'
ftd_gen_prod_db_for_ns = summary_dir + '/ftd-gen-prod-drivers-based-for-ns.pkl'
ftd_ap_prod_eco_prof_db = summary_dir + '/ftd-ap-prod-eco-prof-drivers-based.pkl'
ftd_ns_prod_eco_prof_db = summary_dir + '/ftd-ns-prod-eco-prof-drivers-based.pkl'