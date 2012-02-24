#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
from voronoi import voronoi
import matplotlib.pyplot as plt

X = np.random.uniform(0.0,1.0,100)
Y = np.random.uniform(0.0,1.0,100)
cells, triangles, circles = voronoi(X,Y)

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111, aspect=1)

plt.scatter(X, Y, s=10, color='k', zorder=1)
for cell in cells:
    codes = [matplotlib.path.Path.MOVETO] \
        + [matplotlib.path.Path.LINETO] * (len(cell)-2) \
        + [matplotlib.path.Path.CLOSEPOLY]
    path = matplotlib.path.Path(cell,codes)
    patch = matplotlib.patches.PathPatch(
        path, facecolor='none', edgecolor='.5', linewidth=.5)
    axes.add_patch(patch)

plt.axis([0,1,0,1])
plt.xticks([]), plt.yticks([])
plt.show()
