#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.path as path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import MultipleLocator

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, aspect=1,axisbelow=True)
axes.set_xlim(0,4)
axes.set_ylim(0,4)

axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.xaxis.set_minor_locator(MultipleLocator(0.1))
axes.yaxis.set_major_locator(MultipleLocator(1.0))
axes.yaxis.set_minor_locator(MultipleLocator(0.1))

patch = patches.Circle((.65,.65), radius=.25, transform=axes.transAxes,
                       facecolor='none', edgecolor='black',zorder=1)
axes.grid(which='major', axis='x', color='0.75',
          linewidth=0.75, linestyle='-', clip_path=patch)
axes.grid(which='minor', axis='x', color='0.75',
          linewidth=0.25, linestyle='-', clip_path=patch)
axes.grid(which='major', axis='y', color='0.75',
          linewidth=0.75, linestyle='-', clip_path=patch)
axes.grid(which='minor', axis='y', color='0.75',
          linewidth=0.25, linestyle='-', clip_path=patch)
axes.add_patch(patch)


plt.show()
