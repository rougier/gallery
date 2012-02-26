#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
from voronoi import voronoi
import matplotlib.pyplot as plt

X,Y = np.meshgrid(np.linspace(-0.1,1.1,25), np.linspace(-0.1,1.1,25))
X = X.ravel() + np.random.uniform(-0.025,0.025,X.size)
Y = Y.ravel() + np.random.uniform(-0.025,0.025,Y.size)
cells, triangles, circles = voronoi(X,Y)

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111, aspect=1)
for cell in cells:
    P = np.array(cell[:-1])
    points, codes = [], []
    for i in range(len(P)+1):
        p1,p2 = P[(i+0) % len(P)], P[(i+1) % len(P)]
        c = (p1+p2)/2.0
        if i == 0:
            codes.append(matplotlib.path.Path.MOVETO)
            points.append(c)
        codes.append(matplotlib.path.Path.LINETO)
        points.append(c)
        codes.append(matplotlib.path.Path.CURVE3)
        points.append(p2)
    codes[-1] = matplotlib.path.Path.CLOSEPOLY
    path = matplotlib.path.Path(points,codes)
    color = np.random.uniform(.4,.9,3)
    patch = matplotlib.patches.PathPatch(
        path, facecolor=color, edgecolor='w', zorder=-1)
    axes.add_patch(patch)

plt.axis([0,1,0,1])
plt.xticks([]), plt.yticks([])
plt.show()
