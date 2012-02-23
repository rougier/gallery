#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
Y = np.linspace(0,1,12)
X = np.ones(Y.size)

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
for i in range(7):
    axes.plot( (1+i)*X, Y, linewidth=4)

axes.set_xlim(0,8)
axes.set_yticks([])
axes.set_xticks(np.arange(1,8))

plt.show()
