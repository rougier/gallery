#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib, matplotlib.pyplot as plt

matplotlib.rc('axes', linewidth = 1.5)
matplotlib.rc('axes', linewidth = 1.5)
matplotlib.rc('lines', markeredgewidth=1.5)
matplotlib.rc('xtick', direction = 'out')
matplotlib.rc('ytick', direction = 'out')
matplotlib.rc('xtick.major', size=10)
matplotlib.rc('ytick.major', size=10)

# Data to be represented
X = np.linspace(0,+2*np.pi,256)
Y = np.sin(X*X)*np.exp(-X/3)

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
axes.plot(X,Y, color = 'blue', linewidth=2.0, linestyle="-")

axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')
axes.grid()

plt.show()
