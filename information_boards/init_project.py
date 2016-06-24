from __future__ import division
import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/..')
#
from taxi_common.init_project import get_taxi_home_path, get_taxi_data_path  # @UnresolvedImport
taxi_home, taxi_data = get_taxi_home_path(), get_taxi_data_path()
# Trip mode
DIn_PIn, DIn_POut, DOut_PIn, DOut_POut = range(4)
# Units
SEC3600, SEC60 = 60 * 60, 60
CENT = 100
#
DAY_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
TIME_SLOTS = range(24)
#
# summary
#
summary_dir = taxi_data + '/summary'