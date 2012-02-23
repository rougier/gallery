#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# Data to be represented
X = np.linspace(2000,2010,100)
Y = np.sin(X/2)
Y = 500 + 500*(Y-Y.min())/(Y.max()-Y.min())

matplotlib.rc('font', family = 'sans')
matplotlib.rc('font', size = '10')
matplotlib.rc('axes', facecolor = 'white')
matplotlib.rc('lines', markeredgewidth = 1.0)
matplotlib.rc('grid', color='white')
matplotlib.rc('grid', linewidth=1)
matplotlib.rc('grid', linestyle='-')
matplotlib.rc('xtick.major', size = 0.0)
matplotlib.rc('xtick.minor', size = 0.0)
matplotlib.rc('xtick', color='w')
matplotlib.rc('ytick', direction = 'out')
matplotlib.rc('ytick.major', size = 10)

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes= plt.subplot(111, axisbelow=True)
axes.plot(X, Y, color = '0.25', linewidth=1.5, linestyle="-")
axes.fill_between(X, 0, Y, color = '0.85', zorder=-1)
axes.set_xlim(2000, 2010)
axes.set_ylim( 0, 1100)

axes.set_yticks([0,500,1000,1100])
axes.spines['left'].set_color('none')
axes.spines['top'].set_color('none')
axes.spines['bottom'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('right')
axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.xaxis.set_minor_locator(MultipleLocator(0.5))
axes.grid(which='major', axis='x', linewidth=1.0)
axes.grid(which='minor', axis='x', linewidth=0.5)
for label in axes.get_xticklabels():
    label.set_color('k')
plt.show()
