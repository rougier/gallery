#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.patheffects as PathEffects

def plot(X,Y):
    # Parameterize curve
    L = np.zeros(len(X))
    L[1:] = np.sqrt((X[1:] - X[:-1])**2 + (Y[1:] - Y[:-1])**2)
    l = L.sum()
    T = np.cumsum(L)
    X_,Y_ = [],[]
    for t in np.linspace(0,l,100):
        i = np.argmax((T-t)>=0)
        a,Xa,Ya = T[i], X[i], Y[i]
        if i > 0:
            b = T[i-1]
            Xb = X[i-1]
            Yb = Y[i-1]
            r = (t-a)/(b-a)
            x,y = (1-r)*Xa + r*Xb, (1-r)*Ya + r*Yb
        else:
            x,y = Xa,Ya
        X_.append(x)
        Y_.append(y)

    # Plot
    axes = plt.gca()

    # Iterate every 10 points
    for i in range(0,100,10):
        
        # Plot line (6 vertices)
        verts = [(X_[i+j],Y_[i+j]) for j in range(0,6)]
        codes = [Path.MOVETO ] + [Path.LINETO ]*(6-1)
        path = Path(verts, codes)

        # Outer 
        patch = patches.PathPatch(path, facecolor='none', lw=8.0, transform=axes.transData)
        patch.set_path_effects([PathEffects.Stroke(capstyle='round', foreground='r')])
        axes.add_patch(patch)
        
        # Inner
        patch = patches.PathPatch(path, facecolor='none', lw=6.0, transform=axes.transData)
        patch.set_path_effects([PathEffects.Stroke(capstyle='round', foreground='w')])
        axes.add_patch(patch)

    axes.set_xlim(1.05*X.min(), 1.05*X.max())
    axes.set_ylim(1.05*Y.min(), 1.05*Y.max())


fig = plt.figure(figsize=(8,6))
axes = plt.subplot(111)
X = np.linspace(0,2*np.pi, 100)
Y = np.sin(X)
plot(X,Y)
plt.show()
