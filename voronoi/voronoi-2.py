#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
from voronoi import voronoi
import matplotlib.pyplot as plt

X = np.random.uniform(0.0,1.0,50)
Y = np.random.uniform(0.0,1.0,50)
cells, triangles, circles = voronoi(X,Y)

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111, aspect=1)

plt.scatter(X, Y, s=20, color='k', zorder=1)
plt.triplot(X, Y, triangles, lw=0.5, color='.5')
plt.axis([0,1,0,1])
plt.xticks([]), plt.yticks([])
plt.show()
