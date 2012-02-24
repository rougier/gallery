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
axes = plt.subplot(111,aspect=1)
axes.plot( X, Y*0.1, color = 'blue', linewidth=2, linestyle="-" )
axes.plot( X, Y*0.2, color = 'blue', linewidth=2, linestyle="--" )
axes.plot( X, Y*0.3, color = 'blue', linewidth=2, linestyle="-." )
axes.plot( X, Y*0.4, color = 'blue', linewidth=2, linestyle=":" )
line, = axes.plot( X, Y*0.5, color = 'blue', linewidth=2, linestyle="-" )
line.set_dashes([20,2])
line, = axes.plot( X, Y*0.6, color = 'blue', linewidth=2, linestyle="-" )
line.set_dashes([2,20])
line, = axes.plot( X, Y*0.7, color = 'blue', linewidth=2, linestyle="-" )
line.set_dashes((40,5,5,5))
line, = axes.plot( X, Y*0.8, color = 'blue', linewidth=2, linestyle="-" )
line.set_dashes((40,5,5,5,5,5))
line, = axes.plot( X, Y*0.9, color = 'blue', linewidth=2, linestyle="-" )
line.set_dashes((40,5,5,5,5,5,40,5))


axes.set_xlim(X.min(),X.max())
axes.set_ylim(0,1)
axes.set_xticks([])
axes.set_yticks(np.arange(1,10)/10.0)
axes.set_yticklabels(("-","--","-.",":",
                      "(20,2)", "(2,20)", "(40,5,5,5)",
                      "(40,5,5,5,5,5,5)", "(40,5,5,5,5,40)"))

plt.show()
