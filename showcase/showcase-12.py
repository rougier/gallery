#coding = utf-8
#------------------------
# An implementation of the Domino Shuffling Algorithm on Aztec Diamond Graphs.
#------------------

import random
import matplotlib.pyplot as plt
import matplotlib.patches as mps


class Aztec_Diamond:

    def __init__(self, n):
        """
        Use a dict to represent a tiling of the graph.
        The keys of the dict are the "coordinates" of the unit squares. 
        Each square is specified by its left bottom corner (i, j).
        The j-th row (j from y=-n to y=n-1) has min(n+1+j, n-j) unit squares.
        """
        
        self.order = n
        self.tile = dict()
	# initially all squares are holes, hence assigned with 'None
        self.cells = []
        for j in range(-n, n):
            k = min(n+1+j, n-j)
            for i in range(-k, k):
                self.cells.append((i, j))
                
        self.tile = {cell: None for cell in self.cells}

        
    def delete(self):
        """
        Delete all bad blocks in a tiling.
        A bad block is a pair of dominoes that lie in a 2x2 square
        and move towards each other under the shuffling.
        To find all bad blocks one must start the search from the boundary.
        """
        for i, j in self.cells:
            try:
                if ((self.tile[(i, j)] == 'n'
                     and self.tile[(i+1, j)] == 'n'
                     and self.tile[(i, j+1)] == 's'
                     and self.tile[(i+1, j+1)] == 's')
                    or
                    (self.tile[(i, j)] == 'e'
                     and self.tile[(i, j+1)] == 'e'
                     and self.tile[(i+1, j)] == 'w'
                     and self.tile[(i+1, j+1)] == 'w')):
                        
                    self.tile[(i, j)] = None
                    self.tile[(i+1, j)] = None
                    self.tile[(i, j+1)] = None
                    self.tile[(i+1, j+1)] = None
            except:
                pass
        return self

      
    def slide(self):
	'''
	move each domino one sterp in the partial tiling
	'''
        new_board = Aztec_Diamond(self.order+1)
        for (i, j) in self.cells:
            if self.tile[(i, j)] == 'n':
                new_board.tile[(i, j+1)] = 'n'
            if self.tile[(i, j)] == 's':
                new_board.tile[(i, j-1)] = 's'
            if self.tile[(i, j)] == 'w':
                new_board.tile[(i-1, j)] = 'w'
            if self.tile[(i, j)] == 'e':
                new_board.tile[(i+1, j)] = 'e'

        return new_board

    
    def create(self):
        # To fill in the bad blocks one must start the search from the boundary.
        for i, j in self.cells:
            try:
                if (self.tile[(i, j)] == None
                    and self.tile[(i+1, j)] ==None
                    and self.tile[(i, j+1)] == None
                    and self.tile[(i+1, j+1)] == None):

                    if random.random() > 0.5:
                        # Here we fill the bad blocks with a pair of dominoes leaving each 
                        # other since a bad block in az(n) will be a good block in az(n+1).

                        self.tile[(i, j)] = 's'
                        self.tile[(i+1, j)] = 's'
                        self.tile[(i, j+1)] = 'n'
                        self.tile[(i+1, j+1)] = 'n'
                    else:
                        self.tile[(i, j)] = 'w'
                        self.tile[(i+1, j)] = 'e'
                        self.tile[(i, j+1)] = 'w'
                        self.tile[(i+1, j+1)] = 'e'
            except:
                pass
        return self
      
    def draw(self):
        for (i, j) in self.cells:
	    # we just need to find the leftbottom corner of the black square of each domino
	    # This corner along with the type of the domino determines its position
            if (i+j+self.order) % 2 == 1:
                if self.tile[(i, j)] == 'n':
                    p = mps.Rectangle((i-1,j), 2, 1, fc='r', ec='w', lw=lw)
                    ax.add_patch(p)
                if self.tile[(i,j)] == 's':
                    p = mps.Rectangle((i,j), 2, 1, fc='y', ec='w', lw=lw)
                    ax.add_patch(p)
                if self.tile[(i,j)] == 'w':
                    p = mps.Rectangle((i,j), 1, 2, fc='b', ec='w', lw=lw)
                    ax.add_patch(p)
                if self.tile[(i,j)] == 'e':
                    p = mps.Rectangle((i,j-1), 1, 2, fc='g', ec='w', lw=lw)
                    ax.add_patch(p)
    
        return self
        
        
N = 50
dpi = 100
fig = plt.figure(figsize=(8, 8), dpi=dpi)
lw = dpi * fig.get_figwidth() / (20.0 * (N+1))
ax = fig.add_axes([0, 0, 1, 1], aspect=1)
ax.axis('off')
ax.axis([-N-1, N+1, -N-1, N+1])


az = Aztec_Diamond(0)
for i in range(N):
    az = az.delete().slide().create()
print('saving image with matplotlib...')
az.draw()
fig.savefig('random_tiling.png')
print('done!')
