#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator


fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, aspect=1)
axes.set_xlim(0,4)
axes.set_ylim(0,4)

minor = FixedLocator(np.linspace(2,3,10))
major = FixedLocator(np.linspace(2,3,2))
axes.xaxis.set_major_locator(major)
axes.xaxis.set_minor_locator(minor)
axes.yaxis.set_major_locator(major)
axes.yaxis.set_minor_locator(minor)

axes.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
axes.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
axes.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

plt.show()
