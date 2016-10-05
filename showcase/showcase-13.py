#coding = utf-8

import numpy as np
import matplotlib.pyplot as plt

max_iterations = 500
radius = 50
figsize = (8, 6.4)
dpi = 100

def color(z, i):
    """
    assign a RGB color to a complex number z according to its escaping time i
    """
    v = np.log2( i + 1 - np.log2(np.log2(abs(z))) ) / 5
    if v < 1:
        return v**4, v**2.5, v
    else:
        v = max(0, 2-v)
        return v, v**1.5, v**3
    
def mandel(c):
    z = 0
    for i in range(max_iterations):
        if abs(z) > radius:
            return color(z, i)
        z = z**2 + c
    return 0,0,0
        
y, x = np.ogrid[-1.16:1.17:figsize[1]*dpi*1j, -2.1:0.8:figsize[0]*dpi*1j]
z = x+y*1j
R,G,B = np.array(np.frompyfunc(mandel, 1, 3)(z)).astype(np.float)
RGB = np.dstack((R, G, B))
fig = plt.figure(figsize=figsize, dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1], aspect=1)
ax.axis("off")
ax.imshow(RGB)
fig.savefig("Mandelbrot_Smooth_Coloring.png")
