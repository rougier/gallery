#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

# Data to be represented
X = np.linspace(1,9,9)
Y = 5+np.sin(X)

matplotlib.rc('axes', facecolor = '0.9')
matplotlib.rc('axes', linewidth  = 2.0)
matplotlib.rc('xtick.major', pad = -30.0)
matplotlib.rc('xtick.major', size = 40.0)
matplotlib.rc('xtick', direction = 'out')
matplotlib.rc('xtick', color = 'black')
matplotlib.rc('lines', markeredgewidth = 1.5)

fig = plt.figure(figsize=(8,6), dpi=72,facecolor='w')

def plot(axes, title, X,Y):
    axes.plot(X, Y, color = 'blue', linewidth=1.5, linestyle="-",
              marker='o', markerfacecolor='w', markeredgecolor='b',
              markeredgewidth=1.5, markersize=12)
    axes.set_xlim(0, 10)
    axes.set_xticks([])
    axes.set_ylim(0, 10)
    axes.set_yticks([])
    axes.spines['right'].set_color('none')
    axes.spines['top'].set_color('none')
    axes.spines['bottom'].set_color('none')
    axes.yaxis.set_ticks_position('left')
    axes.set_ylabel(title, size=24, rotation='horizontal')
    for i in range(1,10):
        axes.axvline(i,0,10, color='w', linewidth=1.5, zorder=-1)

axes = plt.subplot(611)
plot(axes, "A", X, Y)
axes = plt.subplot(612)
plot(axes, "B", X, Y+np.random.uniform(-2,2,Y.size))
axes = plt.subplot(613)
plot(axes, "C", X, Y+np.random.uniform(-2,2,Y.size))
axes = plt.subplot(614)
plot(axes, "D", X, Y+np.random.uniform(-2,2,Y.size))
axes = plt.subplot(615)
plot(axes, "E", X, Y+np.random.uniform(-2,2,Y.size))

axes.xaxis.set_ticks_position('bottom')
axes.set_xticks(np.arange(1,10))
axes.set_xticklabels(['\n%d' % (2000+y) for y in np.arange(1,10)])
for label in axes.get_xticklabels():
    label.set_verticalalignment('top')
    label.set_horizontalalignment('left')
    label.set_rotation(90)

plt.show()
