import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter

# Read the data from the file
data = np.loadtxt('collatz_data/clz_terms.dat')

# Extract columns
r = data[:, 0]
theta = data[:, 1]
z = data[:, 2]

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a grid for interpolation
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)

# Interpolate the data to create a smooth surface
zi = griddata((x, y), z, (xi, yi), method='cubic')

# Apply a Gaussian filter to smooth the surface and eliminate extrema
zi = gaussian_filter(zi, sigma=1)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the interpolated data as a 3D surface
surf = ax.plot_surface(xi, yi, zi, cmap='viridis', edgecolor='none')

# Add a color bar which maps values to colors
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

# Set the title and labels
ax.set_title('')
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

# Show the plot
plt.show()