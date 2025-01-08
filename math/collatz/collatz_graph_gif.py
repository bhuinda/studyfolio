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

# Create a figure and 3D axis
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Function to update the plot
def update_plot(frame):
    ax.clear()  # Clear the entire axis
    ax.plot(x[:frame], y[:frame], z[:frame], color='b')
    # Set the title and labels
    ax.set_title('Collatz Terms 3D Visualization')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z (steps)')
    # Set axis limits
    ax.set_xlim([x.min(), x.max()])
    ax.set_ylim([y.min(), y.max()])
    ax.set_zlim([z.min(), z.max()])
    return ax,

# Create the animation
num_frames = len(x)
ani = animation.FuncAnimation(fig, update_plot, frames=num_frames, interval=50, blit=False)

# Save the animation as a GIF using PillowWriter
ani.save('collatz_terms.gif', writer='pillow', fps=20)

# Show the plot
plt.show()