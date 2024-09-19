"""
visualize grid map layers
"""
import numpy as np
import matplotlib.pyplot as plt

fileName = '/home/aiyang/groundgrid/maxHeight.txt'
grid = []
with open(fileName, 'r') as file:
    for line in file:
        grid.append([float(x) for x in line.split()])
grid = np.array(grid)

vmin = 0
vmax = 1
print(grid)

plt.imshow(grid, interpolation='none', vmin=vmin, vmax=vmax)
plt.colorbar(label='Value')
plt.title('Grid Visualization (m2)')
plt.show()