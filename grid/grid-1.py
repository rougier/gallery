#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8,6), dpi=72,facecolor="white")
axes = plt.subplot(111, aspect=1)
axes.set_xlim(0,4)
axes.set_ylim(0,4)

axes.grid(axis='both')

plt.show()
