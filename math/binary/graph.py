# import numpy as np
# import matplotlib.pyplot as plt
# import numpy.linalg as la

# # Midpoints and slopes
# x_midpoints = np.array([0.75, 1.25, 1.75, 2.25, 2.75])
# slopes = np.array([5.78, 6.152, 5.826, 5.678, 5.606])

# # Matrix A and vector b
# A = np.array([[x**2, x, 1] for x in x_midpoints])
# b = slopes

# # Solve for coefficients [a, b, c]
# coefficients = la.lstsq(A, b, rcond=None)[0]
# a, b, c = coefficients

# # Polynomial expression
# print(f"Polynomial: {a:.5f}x^2 + {b:.5f}x + {c:.5f}")

# # Generate x and y values for plotting
# x_vals = np.linspace(0.5, 3, 500)
# y_vals = a * x_vals**2 + b * x_vals + c

# # Plot the slopes and polynomial fit
# plt.figure(figsize=(8, 6))
# plt.scatter(x_midpoints, slopes, color="red", label="Original Slopes (Data Points)")
# plt.plot(x_vals, y_vals, color="blue", label="Quadratic Fit")
# plt.title("Quadratic Polynomial Fit for Slopes")
# plt.xlabel("x (Midpoints)")
# plt.ylabel("Slope")
# plt.legend()
# plt.grid(True)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

# Midpoints for prime number theorem
x_midpoints = np.array([10, 20, 30, 40, 50])
slopes = np.array([1 / np.log(x) for x in x_midpoints])

# Matrix A and vector b
A = np.array([[x**2, x, 1] for x in x_midpoints])
b = slopes

# Solve for coefficients [a, b, c]
coefficients = la.lstsq(A, b, rcond=None)[0]
a, b, c = coefficients

# Polynomial expression
print(f"Polynomial: {a:.5f}x^2 + {b:.5f}x + {c:.5f}")

# Generate extended x and y values for plotting
x_vals = np.linspace(5, 60, 1000)  # Extended range
y_vals = a * x_vals**2 + b * x_vals + c

# Plot the PNT slopes and polynomial fit
plt.figure(figsize=(10, 8))
plt.scatter(x_midpoints, slopes, color="red", label="PNT Slopes (Data Points)")
plt.plot(x_vals, y_vals, color="blue", label="Quadratic Fit")
plt.title("Quadratic Polynomial Fit for PNT Slopes")
plt.xlabel("x (Midpoints)")
plt.ylabel("Slope")
plt.legend()
plt.grid(True)
plt.show()