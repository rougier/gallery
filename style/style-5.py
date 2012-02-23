#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linspace(0,1,10)
Y = np.ones(X.size)
patterns = ('/','//','-', '+', 'x', '\\', '\\\\', '*', 'o', 'O', '.')

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
for i,pattern in enumerate(patterns):
    axes.bar( .5+i, 1, hatch=pattern, color='white', edgecolor='blue',)
axes.set_xlim(0,len(patterns)+.5)
axes.set_ylim(0,1)

axes.set_yticks([])
axes.set_xticks(np.arange(1,len(patterns)+1))
axes.set_xticklabels(patterns)

plt.show()
