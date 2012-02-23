#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
Z = np.random.uniform(0,1,(5,5))
interpolations = ['nearest',  'bilinear', 'bicubic', 'spline16',
                  'spline36', 'hanning',  'hamming', 'hermite',
                  'kaiser',   'quadric',  'catrom',  'gaussian',
                  'bessel',   'mitchell', 'sinc',    'lanczos']

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
for i,interpolation in enumerate(interpolations):
    axes = plt.subplot(4,4,i+1)
    axes.imshow(Z, interpolation=interpolation)
    axes.set_xticks([])
    axes.set_yticks([])
    axes.set_title(interpolation, size=10)

plt.show()
