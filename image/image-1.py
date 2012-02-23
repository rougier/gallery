#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Data to be represented
Z = np.random.uniform(0,1,(5,5))

# Actual plotting
fig = plt.figure(figsize=(8,6), dpi=72, facecolor="white")
axes = plt.subplot(111)
axes.imshow(Z, interpolation='nearest')
axes.grid()
plt.show()
