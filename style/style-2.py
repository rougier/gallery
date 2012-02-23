#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linspace(0,1,10)
Y = np.ones(X.size)

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
axes.plot( X, Y*0.2, color = 'blue', linewidth=2, linestyle="-" )
axes.plot( X, Y*0.4, color = 'blue', linewidth=2, linestyle="--" )
axes.plot( X, Y*0.6, color = 'blue', linewidth=2, linestyle="-." )
axes.plot( X, Y*0.8, color = 'blue', linewidth=2, linestyle=":" )

axes.set_xlim(X.min(),X.max())
axes.set_ylim(0,1)
axes.set_xticks([])
axes.set_yticks((0.2,0.4,0.6,0.8))
axes.set_yticklabels(("-","--","-.",":","."))

plt.show()
