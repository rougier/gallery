#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
import matplotlib
import matplotlib.path as path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MultipleLocator

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, aspect=1, axisbelow=True)

lena = np.array(Image.open("lena.png"))
im = plt.imshow(lena, origin = 'upper', interpolation='nearest')
axes.set_xticks([])
axes.set_yticks([])

axes = plt.axes([0.05,0.00,0.40,0.50], frameon=False)
patch1 = patches.Circle((.5,.5), radius=.45, transform=axes.transAxes,
                        linewidth=2, facecolor='none', edgecolor='black',zorder=2)
patch2 = patches.Circle((.5,.5), radius=.46, transform=axes.transAxes,
                        linewidth=2, facecolor='white', edgecolor='white',zorder=1)
im = plt.imshow(lena[215:315,285:385], origin = 'upper', zorder=3,
                interpolation='nearest', clip_path=patch1)
axes.set_xticks([])
axes.set_yticks([])
axes.add_patch(patch1)
axes.add_patch(patch2)

plt.show()
