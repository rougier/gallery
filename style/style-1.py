#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
Y = np.linspace(0,1,12)
X = np.ones(Y.size)
W = [0.25,0.50,0.75,1,2,3,4,5,6,7,8]

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor='white')
axes = plt.subplot(111)
for i,w in enumerate(W):
    axes.plot( (1+i)*X, Y, linewidth=w, color='blue')

axes.set_xlim(0,len(W)+1)
axes.set_yticks([])
axes.set_xticks(np.arange(1,len(W)+1))
axes.set_xticklabels(['%.2f' % w for w in W])

plt.show()
