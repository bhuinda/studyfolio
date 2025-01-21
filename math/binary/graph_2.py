# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.linalg import expm

# # Constants
# hbar = 1.0  # Planck's constant (scaled)
# m1, m2 = 1.0, 1.0  # Masses of the pendulums
# l1, l2 = 1.0, 1.0  # Lengths of the pendulums
# g = 9.8  # Gravitational acceleration

# # Discretization
# theta_max = np.pi  # Max angle (radians)
# grid_points = 100  # Number of grid points

# theta = np.linspace(-theta_max, theta_max, grid_points)
# d_theta = theta[1] - theta[0]

# # Create 2D grid for theta_1 and theta_2
# theta_1, theta_2 = np.meshgrid(theta, theta)

# # Hamiltonian construction
# # Kinetic term: p^2 / (2 * I)
# I1 = m1 * l1**2
# I2 = m2 * l2**2

# def kinetic_term(grid_points, I):
#     diag = np.ones(grid_points)
#     off_diag = -0.5 * np.ones(grid_points - 1)
#     kinetic = np.diag(diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)
#     return -hbar**2 / (2 * I * d_theta**2) * kinetic

# K1 = kinetic_term(grid_points, I1)
# K2 = kinetic_term(grid_points, I2)

# # Potential term: -m * g * l * cos(theta)
# V1 = -m1 * g * l1 * np.cos(theta_1)
# V2 = -m2 * g * (l1 * np.cos(theta_1) + l2 * np.cos(theta_2))
# V = V1 + V2

# # Combine Hamiltonian (K1 + K2 + V)
# H = np.kron(K1, np.eye(grid_points)) + np.kron(np.eye(grid_points), K2) + np.diag(V.flatten())

# # Initial wavefunction (Gaussian packet)
# def initial_wavefunction(theta_1, theta_2, theta1_0=0, theta2_0=0, sigma=0.1):
#     psi = np.exp(-((theta_1 - theta1_0)**2 + (theta_2 - theta2_0)**2) / (2 * sigma**2))
#     return psi / np.sqrt(np.sum(np.abs(psi)**2))  # Normalize

# psi_0 = initial_wavefunction(theta_1, theta_2)

# # Time evolution
# T = 10  # Total time
# dt = 0.01  # Time step
# time_steps = int(T / dt)

# # Evolve using the matrix exponential
# psi_t = psi_0.flatten()
# probabilities = []

# for t in range(time_steps):
#     U = expm(-1j * H * dt / hbar)  # Time evolution operator
#     psi_t = U @ psi_t
#     probabilities.append((np.abs(psi_t)**2).reshape(grid_points, grid_points))

# # Visualization
# # Plot initial and final probability density
# plt.figure(figsize=(12, 6))
# plt.subplot(1, 2, 1)
# plt.title("Initial Probability Density")
# plt.contourf(theta, theta, probabilities[0], levels=50, cmap='viridis')
# plt.colorbar(label='Probability Density')
# plt.xlabel("Theta 1 (rad)")
# plt.ylabel("Theta 2 (rad)")

# plt.subplot(1, 2, 2)
# plt.title("Final Probability Density")
# plt.contourf(theta, theta, probabilities[-1], levels=50, cmap='viridis')
# plt.colorbar(label='Probability Density')
# plt.xlabel("Theta 1 (rad)")
# plt.ylabel("Theta 2 (rad)")

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

right_angle_deg = 90.0000109  # Degrees
right_angle_rad = right_angle_deg * (np.pi / 180)  # Convert to radians

# Example of usage: Initial conditions near the precise right angle


# Constants
g = 9.8  # Gravitational acceleration (m/s^2)
l1, l2 = 1.0, 1.0  # Lengths of the pendulum arms (m)
m1, m2 = 1.0, 1.0  # Masses of the pendulum bobs (kg)

# Equations of motion
def equations_of_motion(t, y):
    """Compute derivatives for the double pendulum."""
    theta1, z1, theta2, z2 = y  # Unpack variables

    # Auxiliary calculations
    delta = theta2 - theta1
    denom1 = (m1 + m2) * l1 - m2 * l1 * np.cos(delta)**2
    denom2 = (l2 / l1) * denom1

    # Angular accelerations
    theta1_ddot = (
        (m2 * g * np.sin(theta2) * np.cos(delta) - m2 * np.sin(delta) * l2 * z2**2 - (m1 + m2) * g * np.sin(theta1)) / denom1
    )
    theta2_ddot = (
        ((m1 + m2) * (l1 * z1**2 * np.sin(delta) - g * np.sin(theta2) + g * np.sin(theta1) * np.cos(delta)) + m2 * l2 * z2**2 * np.sin(delta) * np.cos(delta)) / denom2
    )

    return [z1, theta1_ddot, z2, theta2_ddot]

# Initial conditions
# theta1_0 = np.pi / 4  # Initial angle for pendulum 1 (rad)
# theta2_0 = np.pi / 2  # Initial angle for pendulum 2 (rad)
theta1_0 = right_angle_rad  # Use the precise right angle
theta2_0 = right_angle_rad / 2  # Half of the precise right angle
omega1_0 = 0.0  # Initial angular velocity for pendulum 1 (rad/s)
omega2_0 = 0.0  # Initial angular velocity for pendulum 2 (rad/s)

initial_conditions = [theta1_0, omega1_0, theta2_0, omega2_0]

# Time span
t_span = (0, 20)  # Time range (s)
t_eval = np.linspace(t_span[0], t_span[1], 2000)  # Time points for evaluation

# Solve the equations of motion
solution = solve_ivp(equations_of_motion, t_span, initial_conditions, t_eval=t_eval, method='RK45')

# Extract results
t = solution.t
theta1, theta2 = solution.y[0], solution.y[2]

# Convert to Cartesian coordinates for visualization
x1 = l1 * np.sin(theta1)
y1 = -l1 * np.cos(theta1)

x2 = x1 + l2 * np.sin(theta2)
y2 = y1 - l2 * np.cos(theta2)

# Visualization
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label="Pendulum 1 Path", alpha=0.7)
plt.plot(x2, y2, label="Pendulum 2 Path", alpha=0.7)
plt.title("Double Pendulum Trajectories")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()
plt.show()

# Optional: Animate the double pendulum
def animate_pendulum():
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.grid()

    line1, = ax.plot([], [], 'o-', lw=2, label="Pendulum 1")
    line2, = ax.plot([], [], 'o-', lw=2, label="Pendulum 2")

    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        return line1, line2

    def update(frame):
        i = frame
        line1.set_data([0, x1[i]], [0, y1[i]])
        line2.set_data([x1[i], x2[i]], [y1[i], y2[i]])
        return line1, line2

    ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=10)
    plt.legend()
    plt.show()

# Uncomment to animate
animate_pendulum()
