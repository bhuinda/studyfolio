import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Read the data from the file
data = np.loadtxt('collatz_data/clz_terms.dat')

# Extract columns
r = data[:, 0]
theta = data[:, 1]
z = data[:, 2]

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Normalize the data to a smaller range
x = (x - x.min()) / (x.max() - x.min())
y = (y - y.min()) / (y.max() - y.min())
z = (z - z.min()) / (z.max() - z.min())

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define the window size for the sliding window
window_size = 100

# Calculate the global extrema for each integer value of z
unique_z = np.unique(np.floor(z))
circles = []
for z_val in unique_z:
    mask = np.floor(z) == z_val
    max_radius = np.sqrt(np.max(x[mask]**2 + y[mask]**2))
    theta_circle = np.linspace(0, 2 * np.pi, 100)
    x_circle = max_radius * np.cos(theta_circle)
    y_circle = max_radius * np.sin(theta_circle)
    z_circle = np.full_like(x_circle, z_val / z.max())  # Normalize z value
    circles.append((x_circle, y_circle, z_circle))

# Function to update the plot
def update_plot(frame):
    ax.clear()  # Clear the entire axis
    start = max(0, frame - window_size)
    ax.scatter(x[start:frame], y[start:frame], z[start:frame], color='b', s=10)
    for i in range(start, frame - 1):
        ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color='b')
    # Draw circles
    for x_circle, y_circle, z_circle in circles:
        ax.plot(x_circle, y_circle, z_circle, color='r', linestyle='--')
    # Set the title and labels
    ax.set_title('Collatz Terms 3D Topological Visualization')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z (steps)')
    # Set axis limits
    ax.set_xlim([0, 1])
    ax.set_ylim([0, 1])
    ax.set_zlim([0, 1])
    return ax,

# Create the animation
num_frames = len(x)
ani = animation.FuncAnimation(fig, update_plot, frames=num_frames, interval=50, blit=False)

# Save the animation as a GIF using PillowWriter
ani.save('collatz_terms.gif', writer='pillow', fps=20)

# Show the plot
plt.show()