#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(x = 2*np.cos(np.linspace(0,2*np.pi,2500))
              + np.random.normal(0,0.25,2500),
            y = 2*np.sin(np.linspace(0,2*np.pi,2500))
              + np.random.normal(0,0.25,2500),
            s=50, c="purple", alpha= 0.1, edgecolors='none')
plt.show()
