#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ----------
# Data to be represented

products = ['Vendor A - Product A', 'Vendor A - Product B', 'Vendor A - Product C',
            'Vendor B - Product A', 'Vendor B - Product B', 'Vendor B - Product C',
            'Vendor C - Product A', 'Vendor C - Product B', 'Vendor C - Product C']

values = np.random.uniform(10,60,len(products))

# ----------

# Choose some nice colors
matplotlib.rc('axes', facecolor = '#6E838A')
matplotlib.rc('axes', edgecolor = '#737373')
matplotlib.rc('axes', linewidth = 1)
matplotlib.rc('ytick', direction='out')
matplotlib.rc('xtick', direction='out')
matplotlib.rc('figure.subplot', left=0.25)

# Make figure background the same colors as axes
fig = plt.figure(figsize=(8,6), facecolor='#6E838A')

# Remove left and top axes spines
axes = plt.subplot(1,1,1)
axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')
axes.xaxis.set_ticks_position('bottom')
axes.yaxis.set_ticks_position('left')

# Adjust yticks to the number of products
plt.yticks(np.arange(len(products)+1), [])

# Set tick labels color to white
for label in axes.get_xticklabels()+axes.get_yticklabels():
    label.set_color('white')

# Set tick labels line width to 1
for line in axes.get_xticklines() + axes.get_yticklines():
    line.set_markeredgewidth(1)

# Set axes limits
ymin, ymax = 0, len(products)
xmin, xmax = 0, 60
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)

# Start with blue colormap
cmap = plt.cm.Blues

for i, label in enumerate(products):

    # Alternate band of light background
    if not i%2:
        p = patches.Rectangle(
            (0, i), xmax, 1, fill=True, transform=axes.transData,
            lw=0, facecolor='w', alpha=.1)
        axes.add_patch(p)

    # Product name left to the axes
    plt.text(-.5, i+0.5, label, color="white", size=10,
             horizontalalignment='right', verticalalignment='center')

    # Plot the bar with gradient (1 to .65)
    value = values[i]
    X = np.array([1,.65]).reshape((1,2))
    axes.imshow(X,extent=(0,value,i+.25,i+.75),cmap=cmap, vmin=0, vmax=1)
    plt.text(value-0.5, i+0.5, '%.1f' % value, color="white", size=10,
             horizontalalignment='right', verticalalignment='center')

    # Change colormap every 3 values
    if i >= 2: cmap = plt.cm.Greens
    if i >= 5: cmap = plt.cm.Reds

# Set a nice figure aspect
axes.set_aspect(4.5)

# Write some title & subtitle
plt.text(1, 10.0, "Vendor benchmarks", color="1.0", fontsize=14)
plt.text(1,  9.7, "(higher is better)", color="0.75", fontsize=10)

# Done
matplotlib.rc('savefig', facecolor = '#6E838A')
plt.show()
