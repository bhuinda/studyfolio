def decimal_to_binary_string(decimal):
  """
  Converts a decimal number to binary representation 
  where integers are treated as strings and the decimal 
  is represented by the concatenation symbol "+".

  Args:
    decimal: The decimal number to convert.

  Returns:
    The binary representation of the decimal number.
  """

  # Separate integer and decimal parts
  integer_part = int(decimal)
  decimal_part = decimal - integer_part

  # Convert integer part to binary
  binary_integer = bin(integer_part)[2:]  # Remove '0b' prefix

  # Convert decimal part to binary (approximate)
  binary_decimal = ""
  while decimal_part > 0 and len(binary_decimal) < 16:  # Limit to 16 decimal places
    decimal_part *= 2
    if decimal_part >= 1:
      binary_decimal += "1"
      decimal_part -= 1
    else:
      binary_decimal += "0"

  # Combine integer and decimal parts using "+" as the separator
  binary_representation = binary_integer + "+" + binary_decimal

  return binary_representation

# Example usage
decimal_number = 51.58
binary_representation = decimal_to_binary_string(decimal_number)
print(f"Decimal: {decimal_number}")
print(f"Binary Representation: {binary_representation}")

'''
+03.00 = 11      + 0000000000000000
-62.92 = 111110  + 1110101110000101
112.04 = 1110000 + 0000101000111101
-51.58 = 110011  + 1001010001111010
'''

# import numpy as np
# import matplotlib.pyplot as plt

# def quartic_polynomial(x):
#     return 3.00*x**4 - 62.92*x**3 + 112.04*x**2 - 51.58*x + 3.00

# def plot_polynomial_powers(x):
#     """
#     Plots each power term of the quartic polynomial.

#     Args:
#       x: Array of x-values.
#     """
#     y_x4 = 3.00 * x**4
#     y_x3 = -62.92 * x**3
#     y_x2 = 112.04 * x**2
#     y_x1 = -51.58 * x
#     y_x0 = np.full_like(x, 3.00)  # Create an array of the same shape as x filled with 3.00

#     plt.plot(x, y_x4, label='3.00x^4')
#     plt.plot(x, y_x3, label='-62.92x^3')
#     plt.plot(x, y_x2, label='112.04x^2')
#     plt.plot(x, y_x1, label='-51.58x')
#     plt.plot(x, y_x0, label='3.00')

#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Polynomial Powers')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# x = np.linspace(-10, 10, 1000)  # Generate x values for plotting
# plot_polynomial_powers(x)

# import numpy as np
# import matplotlib.pyplot as plt

# def quartic_polynomial(x, y):
#     return 3.00*x**4 - 62.92*x**3 + 112.04*x**2 - 51.58*x + 3.00 + y

# # Generate x values (adjust range and step size as needed)
# x = np.linspace(-10, 10, 1000)

# # Plot the polynomial function for different fixed values of y
# y_values = [-10, -5, 0, 5, 10]

# plt.figure(figsize=(10, 8))

# for y in y_values:
#     z = quartic_polynomial(x, y)
#     plt.plot(x, z, label=f'y = {y}')

# plt.xlabel('x')
# plt.ylabel('z')
# plt.title('Elliptical Nature of the Polynomial Function in 2D')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def generate_shifted_functions(num_functions=5):
#     """
#     Generates a list of functions, where each function is a shifted version 
#     of the initial function: f(x) = 3.00x^4 

#     Args:
#       num_functions: The number of functions to generate.

#     Returns:
#       A list of functions.
#     """
#     functions = []
#     y_shift = 0

#     for _ in range(num_functions):
#         functions.append(lambda x, shift=y_shift: 3.00*x**4 + shift)
#         y_shift += 3.00 * (5**4)  # Calculate the y-intercept shift for the next function

#     return functions

# def plot_functions(functions, x_range=(-5, 5)):
#     """
#     Plots the given list of functions.

#     Args:
#       functions: A list of functions to plot.
#       x_range: A tuple defining the range of x-values for plotting.
#     """
#     x = np.linspace(x_range[0], x_range[1], 100)

#     for func in functions:
#         y = func(x)
#         plt.plot(x, y)

#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.title('Shifted Functions')
#     plt.grid(True)
#     plt.show()

# # Generate a list of shifted functions
# functions = generate_shifted_functions(num_functions=5) 

# # Plot the functions
# plot_functions(functions)