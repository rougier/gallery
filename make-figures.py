#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob

gallery = """
Matplotlib gallery
==================

This is a collection of matplotlib samples.

If you want to contribute:

* make sure to put your example in the right directory or create a new one if
  necessary.

* Each example (but the showcases) is supposed to illustrate a concept and the
  source should be small enough such that understanding how things are done is
  easy.

* Try to avoid shortcuts (like 'c' instead of 'color'), this makes things more
  difficult to understand for new comers.

* Try to make your example beautiful, especially for the showcase ones

Repository: https://github.com/rougier/gallery

----

"""
    
figure_rst = """
.. figure:: %s/%s.png
   :target: %s/%s-large.png

   Source `%s.py <%s/%s.py>`_

"""

directories = 'spine', 'style', 'image', 'grid', 'one-line', 'showcase'
for d in directories:
    print "Making all in", d
    for f in glob.glob(d+"/*.py"):
        name = os.path.basename(f)
        name = name.split('.')[0]
        gallery +=  figure_rst % (d,name,d,name,name,d,name)
    print
f = open('gallery.rst','w')
f.write(gallery)
f.close()

