#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
import numpy as np
from voronoi import voronoi
import matplotlib.pyplot as plt
from PIL import Image

X,Y = np.meshgrid(np.linspace(-0.1,1.1,50), np.linspace(-0.1,1.1,50))
X = X.ravel() + np.random.uniform(-0.0125,0.0125,X.size)
Y = Y.ravel() + np.random.uniform(-0.0125,0.0125,Y.size)
cells,triangles,circles = voronoi(X,Y)
lena = np.array(Image.open("lena.png"))

fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111, aspect=1)
for i,cell in enumerate(cells):
    codes = [matplotlib.path.Path.MOVETO] \
        + [matplotlib.path.Path.LINETO] * (len(cell)-2) \
        + [matplotlib.path.Path.CLOSEPOLY]
    path = matplotlib.path.Path(cell,codes)

    x,y = 1-max(min(Y[i],1),0), max(min(X[i],1),0)
    x = int(x*(lena.shape[0]-1))
    y = int(y*(lena.shape[1]-1))
    color = lena[x,y]/256.0
    patch = matplotlib.patches.PathPatch(
        path, facecolor=color, edgecolor='w', linewidth=.5, zorder=-1)
    axes.add_patch(patch)

plt.axis([0,1,0,1])
plt.xticks([]), plt.yticks([])
plt.show()
