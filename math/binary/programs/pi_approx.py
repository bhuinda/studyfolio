# import numpy as np
# import matplotlib.pyplot as plt

# # Define the polynomial based on the given coefficients
# def polynomial(x):
#     return 1 + 2.74825817e+05 * x - 5.77544542e+05 * x**2 + 4.10112208e+05 * x**3 - 1.19753458e+05 * x**4 + 1.23769750e+04 * x**5

# # Generate x values from -5 to 5 (or choose any range you want)
# x_values = np.linspace(-5, 5, 20)  # Reduce the number of points for clarity in print
# y_values = polynomial(x_values)

# # Print x and P(x) values
# print("x\t\tP(x)")
# print("-" * 30)
# for x, y in zip(x_values, y_values):
#     print(f"{x:.2f}\t\t{y:.2e}")

# # Plot the polynomial function
# x_plot = np.linspace(-5, 5, 400)  # Higher resolution for the plot
# y_plot = polynomial(x_plot)

# plt.plot(x_plot, y_plot, label='Polynomial: P(x)')
# plt.axhline(0, color='black', linewidth=1)  # X-axis
# plt.axvline(0, color='black', linewidth=1)  # Y-axis
# plt.xlabel('x')
# plt.ylabel('P(x)')
# plt.title('Polynomial Plot')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# # Define the polynomial function
# def polynomial(x):
#     return 1 + 2.74825817e+05 * x - 5.77544542e+05 * x**2 + 4.10112208e+05 * x**3 - 1.19753458e+05 * x**4 + 1.23769750e+04 * x**5

# # Generate x values
# x = np.linspace(0.1, 5, 400)  # Avoid x=0 to prevent log errors
# P_x = polynomial(x)

# # Compute transformations
# log_P_x = np.log(P_x)         # Log of dependent variable
# ln_x = np.log(x)              # Log of independent variable
# P_ln_x = polynomial(ln_x)     # Polynomial of log-transformed independent variable
# log_P_ln_x = np.log(P_ln_x)   # Log of P(ln(x)) for log-log plot

# # Save numerical results to a CSV file
# csv_path = "./data/polynomial_results.csv"
# with open(csv_path, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["x", "P(x)", "ln(P(x))", "ln(x)", "P(ln(x))", "ln(P(ln(x)))"])
#     for i in range(len(x)):
#         writer.writerow([x[i], P_x[i], log_P_x[i], ln_x[i], P_ln_x[i], log_P_ln_x[i]])

# # Plot 1: ln(P(x)) vs. x
# plt.figure(figsize=(12, 8))
# plt.subplot(3, 1, 1)
# plt.plot(x, log_P_x, label='ln(P(x)) vs. x', color='blue')
# plt.xlabel('x')
# plt.ylabel('ln(P(x))')
# plt.title('Log of Dependent Variable')
# plt.grid(True)
# plt.legend()

# # Plot 2: P(ln(x)) vs. x
# plt.subplot(3, 1, 2)
# plt.plot(x, P_ln_x, label='P(ln(x)) vs. x', color='green')
# plt.xlabel('x')
# plt.ylabel('P(ln(x))')
# plt.title('Log-Transformed Independent Variable')
# plt.grid(True)
# plt.legend()

# # Plot 3: ln(P(ln(x))) vs. ln(x)
# plt.subplot(3, 1, 3)
# plt.plot(ln_x, log_P_ln_x, label='ln(P(ln(x))) vs. ln(x)', color='red')
# plt.xlabel('ln(x)')
# plt.ylabel('ln(P(ln(x)))')
# plt.title('Log-Log Plot')
# plt.grid(True)
# plt.legend()

# # Save the plots as an image file
# png_path = "./data/polynomial_plots.png"
# pdf_path = "./data/polynomial_plots.pdf"
# plt.tight_layout()
# plt.savefig(png_path)  # Save as PNG
# plt.savefig(pdf_path)  # Save as PDF

# # Show the plots
# plt.show()

# (csv_path, png_path, pdf_path)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the polynomial function
def polynomial(x):
    return (1 + 274825.817 * x - 577544.542 * x**2 + 410112.208 * x**3
            - 119753.458 * x**4 + 12376.975 * x**5)

# Generate x values (adjust range and step size as needed)
x = np.linspace(-1, 1, 500)  # x from -1 to 1 with 500 points

# Calculate corresponding y values
y = polynomial(x)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the x and y values
X, Y = np.meshgrid(x, y)
Z = polynomial(X)

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_title("3D Graph of the Polynomial Function")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# Show the plot
plt.show()