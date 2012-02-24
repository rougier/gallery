#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
from voronoi import voronoi
import matplotlib.pyplot as plt

X = np.random.uniform(0.0,1.0,10)
Y = np.random.uniform(0.0,1.0,10)
cells, triangles, circles = voronoi(X,Y)

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111, aspect=1)
plt.scatter(X, Y, s=20, color='k', zorder=1)
for circle in circles:
    x,y,r = circle
    patch = matplotlib.patches.Circle(
        (x,y), radius=r, linewidth=0.5, facecolor='none', edgecolor='0.5')
    axes.add_patch(patch)

plt.axis([0,1,0,1])
plt.xticks([]), plt.yticks([])
plt.show()
