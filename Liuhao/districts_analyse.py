
'''
    对地理位置进行分析
    2019-6-10
'''
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

warnings.simplefilter("ignore")

events = pd.read_csv("../data/data/events.csv",nrows=500000)

plt.figure(1, figsize=(12,6))


#投影法
m1 = Basemap(projection='merc',llcrnrlat=-60,
             urcrnrlat=65,llcrnrlon=-180,
             urcrnrlon=180,lat_0=0,
             resolution='c')

m2 = Basemap(llcrnrlon=70.33,
             llcrnrlat=3.01,
             urcrnrlon=138.16,
             urcrnrlat=56.123,
             resolution='c',
             projection='merc',
             lat_0 = 42.5,
             lon_0 = 120)


#灰色大陆，黑色湖泊
m1.fillcontinents(color='#40de5a',lake_color='#70f3ff')
#m2.fillcontinents(color='#191919',lake_color='#000000')
#黑色背景
m1.drawmapboundary(fill_color='#70f3ff')
#m2.drawmapboundary(fill_color='#000000')
#国界线细白
m1.drawcountries(linewidth=0.1, color="b")
#m2.drawcountries(linewidth=0.1, color="w")
mxy = m1(events["longitude"].tolist(), events['latitude'].tolist())

m1.scatter(mxy[0], mxy[1], s=3, c="#ff4777", lw=0, alpha=1, zorder=5)
#m2.scatter(mxy[0], mxy[1], s=3, c="#1292db", lw=0, alpha=1, zorder=5)
plt.title("Global view of events")
plt.show()