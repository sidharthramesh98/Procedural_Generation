import numpy as np
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter

side = 500
height = 100
sparsity = 100

np.random.seed(10)
randbase = np.random.rand(int(side/sparsity),int(side/sparsity))
z = np.zeros((side,side))
x = range(side)
y = range(side)

for X in range(side):
  for Y in range(side):
    sub_space = randbase[int(X/sparsity),int(Y/sparsity)]*height
    z[X,Y] = np.random.normal(sub_space,sub_space)
    if z[X,Y] <0:
      z[X,Y] = 0

blurred = gaussian_filter(z, sigma=10)

hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')
X, Y = np.meshgrid(x, y)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, blurred)

#ha = plt.axes(projection='3d')
#ha.scatter(x, y, z, c='r',marker='o')
plt.show()