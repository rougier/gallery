#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(x = np.linspace(0,10,2000),
            y = np.sin(np.linspace(0,10,2000)),
            c = [(i,i,i) for i in (1-np.sin(np.linspace(0,np.pi,2000)))],
            s = [i for i in 5*(np.sin(np.linspace(0,np.pi,2000)))],
            edgecolors='none')
plt.show()
