#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
X = np.linspace(0,100,20)
M = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)
W = (1+np.sin(X/20)+np.random.uniform(0.75,1.0,X.size)) * np.linspace(1,0.2,X.size)

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, axisbelow=True)

plt.bar(X, +M, width=5.25, facecolor='#9999ff', edgecolor='white')
for i,x in enumerate(X):
    x += 5.25/2
    y = M[i] + 0.1
    plt.text(x,y,"%.1f" % y, color='#9999ff', size=9,
             horizontalalignment='center',  verticalalignment='bottom')

plt.bar(X, -W, width=5.25, facecolor='#ff9999', edgecolor='white')
for i,x in enumerate(X):
    x += 5.25/2
    y = -W[i] - 0.1
    plt.text(x,y,"%.1f" % (-y), color='#ff9999', size=9,
             horizontalalignment='center',  verticalalignment='top')

axes.set_xlim([0,110])
axes.set_xticks([])
axes.set_yticks([+1,-1])
axes.set_yticklabels(['MEN', 'WOMEN'])
labels = axes.get_yticklabels()
labels[0].set_rotation(90)
labels[0].set_color('#9999ff')
labels[1].set_rotation(90)
labels[1].set_color('#ff9999')

axes.spines['top'].set_color('none')
axes.spines['left'].set_color('none')
axes.spines['right'].set_color('none')
axes.spines['bottom'].set_color('none')
axes.yaxis.set_ticks_position('left')


plt.text(108,2.00,"2012", color='black', size=36,
         horizontalalignment='right', verticalalignment='bottom')
plt.text(108,1.95,"Those figures are\n totally random", color='.75', size=8,
         horizontalalignment='right', verticalalignment='top')

plt.show()
