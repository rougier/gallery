#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, aspect=1, polar=True)
axes.grid(color='k')

xmajor = FixedLocator(np.linspace(np.pi/6,2*np.pi/6,2))
xminor = FixedLocator(np.linspace(np.pi/6,2*np.pi/6,10))
ymajor = FixedLocator(np.linspace(0.5,0.8,2))
yminor = FixedLocator(np.linspace(0.5,0.8,10))

axes.xaxis.set_major_locator(xmajor)
axes.xaxis.set_minor_locator(xminor)
axes.yaxis.set_major_locator(ymajor)
axes.yaxis.set_minor_locator(yminor)

axes.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
axes.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

axes.set_yticklabels([])

plt.show()
