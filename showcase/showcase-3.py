#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ----------
# Data to be represented

diseases   = ['Disease 1', 'Disease 2','Disease 3','Disease 4','Disease 5',
              'Disease 6', 'Disease 7','Disease 8','Disease 9','Disease 10']
men_deaths   = np.random.uniform(50000,100000,len(diseases))
men_cases    = men_deaths+np.random.uniform(10000,50000,len(diseases))
women_deaths = np.random.uniform(50000,100000,len(diseases))
women_cases  = women_deaths+np.random.uniform(10000,50000,len(diseases))

# ----------


# Choose some nice colors
matplotlib.rc('axes', facecolor = 'white')
matplotlib.rc('figure.subplot', wspace=.65)
matplotlib.rc('grid', color='white')
matplotlib.rc('grid', linewidth=1)

# Make figure background the same colors as axes 
fig = plt.figure(figsize=(8,6), facecolor='white')


# --- MEN data ---
axes_left  = plt.subplot(121)

# Keep only top and right spines
axes_left.spines['left'].set_color('none')
axes_left.spines['bottom'].set_color('none')
axes_left.xaxis.set_ticks_position('top')
axes_left.yaxis.set_ticks_position('right')
axes_left.spines['top'].set_position(('data',len(diseases)-.75))
axes_left.spines['top'].set_color('w') 

# Set axes limits
plt.xlim(150000,0)
plt.ylim(0,len(diseases))

# Set ticks labels
plt.xticks([150000, 100000, 50000, 0],
           ['150000', '100000', '50000', 'MEN'])
axes_left.get_xticklabels()[-1].set_weight('bold')
axes_left.get_xticklines()[-1].set_markeredgewidth(0)
for label in axes_left.get_xticklabels():
    label.set_fontsize(10)
plt.yticks([])


# Plot data
for i in range(len(men_deaths)):
    # Death
    value = men_cases[i]
    p = patches.Rectangle(
        (0, i+0.125), value, 0.75, fill=True, transform=axes_left.transData,
        lw=0, facecolor='blue', alpha=0.1)
    axes_left.add_patch(p)
    # New cases
    value = men_deaths[i]
    p = patches.Rectangle(
        (0, i+0.25), value, 0.5, fill=True, transform=axes_left.transData,
        lw=0, facecolor='blue', alpha=0.5)
    axes_left.add_patch(p)

# Add a grid
axes_left.grid()


# --- WOMEN data ---
axes_right = plt.subplot(122, sharey=axes_left)

# Keep only top and left spines
axes_right.spines['right'].set_color('none')
axes_right.spines['bottom'].set_color('none')
axes_right.xaxis.set_ticks_position('top')
axes_right.yaxis.set_ticks_position('left')
axes_right.spines['top'].set_position(('data',len(diseases)-.75))
axes_right.spines['top'].set_color('w') 

# Set axes limits
plt.xlim(0,150000)
plt.ylim(0,len(diseases))

# Set ticks labels
plt.xticks([0, 50000, 100000, 150000],
           ['WOMEN', '50000', '100000', '150000'])
axes_right.get_xticklabels()[0].set_weight('bold')
for label in axes_right.get_xticklabels():
    label.set_fontsize(10)
axes_right.get_xticklines()[1].set_markeredgewidth(0)
plt.yticks([])

# Plot data
for i in range(len(women_deaths)):
    # Death
    value = women_cases[i]
    p = patches.Rectangle(
        (0, i+0.125), value, 0.75, fill=True, transform=axes_right.transData,
        lw=0, facecolor='red', alpha=0.1)
    axes_right.add_patch(p)
    # New cases
    value = women_deaths[i]
    p = patches.Rectangle(
        (0, i+0.25), value, 0.5, fill=True, transform=axes_right.transData,
        lw=0, facecolor='red', alpha=0.5)
    axes_right.add_patch(p)

# Add a grid
axes_right.grid()


# Y axis labels
# We want them to be exactly in the middle of the two y spines
# and it requires some computations
for i in range(len(diseases)):
    x1,y1 = axes_left.transData.transform_point( (0,i+.5))
    x2,y2 = axes_right.transData.transform_point((0,i+.5))
    x,y = fig.transFigure.inverted().transform_point( ((x1+x2)/2,y1) )
    plt.text(x, y, diseases[i], transform=fig.transFigure,
             horizontalalignment='center', verticalalignment='center')


# Devil hides in the details...
arrowprops = dict(arrowstyle="-", connectionstyle="angle,angleA=0,angleB=90,rad=0")
x = men_cases[0]
axes_left.annotate('NEW CASES', xy=(.9*x, .5),  xycoords='data',
                   horizontalalignment='right', fontsize= 10,
                   xytext=(-40, -3), textcoords='offset points',
                   arrowprops=arrowprops)

x = men_deaths[0]
axes_left.annotate('DEATHS', xy=(.9*x, .5),  xycoords='data',
                   horizontalalignment='right', fontsize= 10,
                   xytext=(-50, -50), textcoords='offset points',
                   arrowprops=arrowprops)

x = women_cases[0]
axes_right.annotate('NEW CASES', xy=(.9*x, .5),  xycoords='data',
                   horizontalalignment='left', fontsize= 10,
                   xytext=(+40, -3), textcoords='offset points',
                   arrowprops=arrowprops)

x = women_deaths[0]
axes_right.annotate('DEATHS', xy=(.9*x, .5),  xycoords='data',
                   horizontalalignment='left', fontsize= 10,
                   xytext=(+50, -50), textcoords='offset points',
                   arrowprops=arrowprops)


# Done
plt.show()
