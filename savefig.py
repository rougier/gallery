#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import matplotlib
matplotlib.use('Agg')
    
f = sys.argv[1]
name = os.path.basename(f)
name = name.split('.')[0]
execfile(f)
plt.savefig('%s.png' % name, dpi=72/4)
plt.savefig('%s-large.png' % name, dpi=72*2)
