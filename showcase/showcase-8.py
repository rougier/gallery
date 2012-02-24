#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Voronoi diagram from a list of points
# Copyright (C) 2011  Nicolas P. Rougier
#
# Distributed under the terms of the BSD License.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def circumcircle(P1,P2,P3):
    ''' 
    Adapted from:
    http://local.wasp.uwa.edu.au/~pbourke/geometry/circlefrom3/Circle.cpp
    '''
    delta_a = P2 - P1
    delta_b = P3 - P2
    epsilon = 0.000000001
    if np.abs(delta_a[0]) <= epsilon and np.abs(delta_b[1]) <= epsilon:
        center_x = 0.5*(P2[0] + P3[0])
        center_y = 0.5*(P1[1] + P2[1])
    else:
        aSlope = delta_a[1]/delta_a[0]
        bSlope = delta_b[1]/delta_b[0]
        if np.abs(aSlope-bSlope) <= epsilon:
            return None
        center_x= (aSlope*bSlope*(P1[1] - P3[1]) + bSlope*(P1[0] + P2 [0]) \
                        - aSlope*(P2[0]+P3[0]) )/(2* (bSlope-aSlope) )
        center_y = -1*(center_x - (P1[0]+P2[0])/2)/aSlope +  (P1[1]+P2[1])/2;
    radius = np.sqrt( (center_x - P1[0])**2+(center_y - P1[1])**2)
    return center_x, center_y, radius

def voronoi(X,Y):
    P = np.zeros((X.size,2))
    P[:,0] = X
    P[:,1] = Y
    D = matplotlib.tri.Triangulation(X,Y)
    T = D.triangles
    n = T.shape[0]
    C = np.zeros((n,3))

    # Get circle for each triangle, center will be a voronoi cell point
    cells = []
    for i in range(X.size):
        cells.append( list() )
    for i in range(n):
        C[i] = circumcircle(P[T[i,0]],P[T[i,1]],P[T[i,2]])
        x,y,r = C[i]
        cells[T[i,0]].append( (x,y) )
        cells[T[i,1]].append( (x,y) )
        cells[T[i,2]].append( (x,y) )

    # Reordering cell points in trigonometric way
    for i,cell in enumerate(cells):
        xy = np.array(cell)
        I = np.argsort(np.arctan2(xy[:,1]-Y[i],xy[:,0]-X[i]))
        cell = xy[I].tolist()
        cell.append(cell[0])
        cells[i] = cell
    return cells

    # X,Y = C[:,0], C[:,1]
    # segments = []
    # for i in range(n):
    #     for j in range(3):
    #         k = D.neighbors[i][j]
    #         if k != -1:
    #             segments.append( [(X[i],Y[i]), (X[k],Y[k])] )
    # return segments, cells


if __name__ == '__main__':
    import matplotlib.path as mpath

    X,Y = np.meshgrid(np.linspace(-0.1,1.1,25), np.linspace(-0.1,1.1,25))
    X = X.ravel() + np.random.uniform(-0.025,0.025,X.size)
    Y = Y.ravel() + np.random.uniform(-0.025,0.025,Y.size)
    cells = voronoi(X,Y)

    fig = plt.figure(figsize=(8,6))
    axes = plt.subplot(111, aspect=1)
    # plt.scatter(X, Y, s=3, color='w', zorder=1)
    for cell in cells:
        codes = [matplotlib.path.Path.MOVETO] \
              + [matplotlib.path.Path.LINETO] * (len(cell)-2) \
              + [matplotlib.path.Path.CLOSEPOLY]
        path = matplotlib.path.Path(cell,codes)
        color = np.random.uniform(.4,.9,3)
        patch = matplotlib.patches.PathPatch(
            path, facecolor=color, edgecolor='w', zorder=-1)
        axes.add_patch(patch)

    plt.axis([0,1,0,1])
    plt.xticks([]), plt.yticks([])
    plt.show()
