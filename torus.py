import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the parameters of torus
R = 2
r = 1

# number of points for the torus
u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, 2*np.pi, 100)
u, v = np.meshgrid(u, v)

# parametric equations for the torus
x = (R+r * np.cos(v)) *np.cos(u)
y = (R+r * np.cos(v)) *np.sin(u)
z = r * np.sin(v)

# create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot the surface
ax.plot_surface(x, y, z, cmap = 'viridis')

#set labels and title
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

#show plot
plt.show()