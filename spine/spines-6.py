#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linspace(-np.pi,+np.pi,256)
Y = np.sin(X)

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111)
axes.plot(X,Y, color = 'blue', linewidth=2, linestyle="-")
axes.set_xlim(1.1*X.min(),1.1*X.max())
axes.set_ylim(1.1*Y.min(),1.1*Y.max())

axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.spines['bottom'].set_position(('data',0))
axes.spines['left'].set_position(('data',0))
axes.set_xticks([])
axes.set_yticks([])

plt.show()
