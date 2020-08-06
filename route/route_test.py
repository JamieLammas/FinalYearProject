#!/usr/bin/env python

import cgi
import cgitb
cgitb.enable()

import matplotlib
matplotlib.use('Agg')

from mpl_toolkits.basemap import Basemap
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import Image
import numpy as np
import csv
import sys

lats = []
longs = []

with open("route.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        lats.append(float(row[0]))
        longs.append(float(row[1]))


fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])

m = Basemap(llcrnrlon=min(longs)-0.001,llcrnrlat=min(lats)-0.001,urcrnrlon=max(longs)+0.001,urcrnrlat=max(lats)+0.001,
            resolution='i', projection='merc', lon_0=longs[0],lat_0=lats[0])

x1, y1 = m(longs, lats)

m.drawmapboundary(fill_color='yellow')
m.scatter(x1, y1, s=5, c='r', marker="o")
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])

#wycombe = np.array(Image.open('/var/www/cgi-bin/final_project/wycombe.png'))
#im = OffsetImage(wycombe, zoom=1)
#ab = AnnotationBbox(im, (x1[-1],y1[-1]), xycoords='data', frameon=False)

#m._check_ax().add_artist(ab)

ax.set_title('GPS Coordinates')

ax.plot(x1, y1)

print "Content-type: image/png\n"

fig.savefig(sys.stdout)

