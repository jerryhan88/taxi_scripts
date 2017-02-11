import __init__
#
from community_analysis import chart_dpath
#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#
# The number of trips depending on hour
#
from taxi_common.file_handling_functions import load_pickle_file
hour_tripNum = load_pickle_file('_hour_tripNum.pkl')
#
_figsize = (8, 6)
_fontsize = 14
_data = hour_tripNum.values()
xTickMarks = hour_tripNum.keys()
_xlabel = 'Hour'
_ylabel = 'The number of trips'
#
fig = plt.figure(figsize=_figsize)
ax = fig.add_subplot(111)
ind = np.arange(len(_data))
width = 0.5  # the width of the bars
#
ax.bar(ind, _data, color='blue')
# axes and labels
ax.set_xlim(-width, len(ind)-width)
ax.set_ylabel(_xlabel)
ax.set_ylabel(_ylabel)
ax.set_xticks(ind)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=_fontsize)

#
# Queueing time distribution
#
from community_analysis import ss_trips_dpath, ss_trips_prefix
df = pd.read_csv('%s/%s0901.csv' % (ss_trips_dpath, ss_trips_prefix))
cn = 'spendingTime'
outlier_set = set(np.where(df[cn] < 0)[0].tolist())
outlier_set = outlier_set.union(set(np.where(df[cn] > df[cn].quantile(0.95))[0].tolist()))
df = df.drop(df.index[list(outlier_set)])
df['queueingTime'] = df[cn] / 60
#
data = df['queueingTime']
_figsize = (8, 6)
_fontsize = 14
x_label, y_label = 'Queueing time (minute)', 'Percent'
num_bin = 10
#
plt.figure(figsize=_figsize)
_, bins, _ = plt.hist(data, num_bin, normed=1, histtype='bar', facecolor='green', alpha=0.75, edgecolor='black')
plt.xlabel(x_label, fontsize=_fontsize); plt.ylabel(y_label, fontsize=_fontsize)
plt.xlim(xmin=0, xmax=data.max())
plt.savefig('%s/%s.pdf' % (chart_dpath, 'queueTimeDist'), bbox_inches='tight', pad_inches=0)



