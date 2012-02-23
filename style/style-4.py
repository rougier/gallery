#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
Y = np.linspace(0,1,12)
X = np.ones(Y.size)
markers = ['.',',','o','v','^','<','>','1','2','3','4',
           's','p','*','h','H','+','x','D','d','|','_', r'$\clubsuit$']

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
for i,marker in enumerate(markers):
    axes.plot( (1+i)*X, Y, color = '0.9', linewidth=1,
               markersize = 13, marker=marker,
               markeredgecolor = '0.10', markerfacecolor = '0.75')

axes.set_xlim(0,len(markers)+1)
axes.set_ylim(Y.min(),Y.max())
axes.set_yticks([])
axes.set_xticks(np.arange(1,len(markers)+1))
axes.set_xticklabels(markers)

plt.show()
