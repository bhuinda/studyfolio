# import matplotlib.pyplot as plt
# import numpy as np
# import math

# def calculate_sequence_and_means_v2(n_terms):
#     """
#     Calculate the sequence using the formula:
#     x_n = (4 * 4^n - 2^n)^2 - (2^n - 1)^2
#     and find the mean between consecutive terms.

#     Args:
#     - n_terms (int): Number of terms to generate.

#     Returns:
#     - sequence (list): List of calculated terms in the sequence.
#     - means (list): List of means between consecutive terms.
#     """
#     sequence = []
#     means = []
#     means_2 = [0.5 * 2]

#     for n in range(0, n_terms + 1):
#         # Calculate x_n using the formula
#         term = (4 * 4**n - 2**n)**2 - (2**n - 1)**2
#         sequence.append(term)
        
#         # Calculate mean between consecutive terms
#         if n >= 1:
#             means.append((sequence[-1] + sequence[-2]) / 2)
#             means_2.append((sequence[-1] / sequence[-2]) / (9 * 2))
    
#     return sequence, means, means_2

# def can_form_triangle(a, b, c):
#     """Check if three sides can form a triangle using the triangle inequality theorem."""
#     return a + b > c and a + c > b and b + c > a

# def calculate_angles(a, b, c):
#     """Calculate the angles of a triangle given its sides using the law of cosines."""
#     angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
#     angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
#     angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
#     return math.degrees(angle_A), math.degrees(angle_B), math.degrees(angle_C)

# # Calculate the sequence and means for 20 terms
# sequence_v2, means_v2, means_v3 = calculate_sequence_and_means_v2(20)

# # Print results
# print("Sequence:", sequence_v2)
# print("Means between terms:", means_v2)
# print("Ratios between terms:", means_v3)

# # Check each consecutive set of 3 numbers in means_v3 to see if they form a triangle
# triangles = []
# for i in range(len(means_v3) - 2):
#     a, b, c = means_v3[i], means_v3[i + 1], means_v3[i + 2]
#     if can_form_triangle(a, b, c):
#         angles = calculate_angles(a, b, c)
#         triangles.append((a, b, c, angles))

# # Print the triangles and their angles
# for i, (a, b, c, angles) in enumerate(triangles):
#     print(f"Triangle {i + 1}: sides = ({a:.2f}, {b:.2f}, {c:.2f}), angles = ({angles[0]:.2f}°, {angles[1]:.2f}°, {angles[2]:.2f}°)")

# # Plot only the means_v3
# plt.figure(figsize=(10, 6))
# plt.plot(means_v3, marker='s', linestyle='-.', color='g', label='Ratios between terms')
# plt.title('Ratios between Consecutive Terms')
# plt.xlabel('Index')
# plt.ylabel('Ratio')
# plt.legend()
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import math

# def calculate_sequence_and_ratio(n_terms):
#     """
#     for ratio f(-1) = 2
#     https://oeis.org/A045668???
#     https://nwchemgit.github.io/P6_3mc.html

#     for ratio f(-1) = ln(4)
#     https://oeis.org/search?q=46+58+77&go=Search
#     https://oeis.org/A133597

#     Calculate the sequence using the formula:
#     x_n = (4 * 4^n - 2^n)^2 - (2^n - 1)^2
#     and find the mean between consecutive terms.

#     Args:
#     - n_terms (int): Number of terms to generate.

#     Returns:
#     - sequence (list): List of calculated terms in the sequence.
#     - means (list): List of means between consecutive terms.
#     - ratios (list): List of ratios between consecutive terms.
#     """
#     sequence = []
#     means = []
#     ratios = [1.38629436112]
#     ratios = [2.00]
#     for n in range(0, n_terms + 1):
#         # term = (4 * 4**n - 2**n)**2 - (2**n - 1)**2
#         # term = (4 * 4**n - 2**(n+1) + 1) * (4 * 4**n - 1)
#         term = 2**(4*n + 4) - 2**(3*n + 3) + 2**(n + 1) - 2**(0)
#         sequence.append(term)
        
#         if n >= 1:
#             means.append((sequence[-1] + sequence[-2]) / 2)  # convergence to 16 via addition-division of a partition function f(n) by a triangular area A := 1/2(3^2 + 3^2); n ≥ 0, n - 1 = ???
#             ratios.append(sequence[-1] / sequence[-2]  / 18) # convergence to 8/9 via division-division of a partition function f(n) by a triangular area A := 1/2(3^2 + 3^2); n ≥ 0, n - 1 = 0.5?
#                                                              # convergence to 31/45 via ... - 0.2

#     return sequence, means, ratios

# def can_form_triangle(a, b, c):
#     """Check if three sides can form a triangle using the triangle inequality theorem."""
#     return a + b > c and a + c > b and b + c > a

# def calculate_angles(a, b, c):
#     """Calculate the angles of a triangle given its sides using the law of cosines."""
#     angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
#     angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
#     angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
#     return math.degrees(angle_A), math.degrees(angle_B), math.degrees(angle_C)

# # Calculate the sequence, means, and ratios for 20 terms
# sequence, means, ratios = calculate_sequence_and_ratio(100)

# # Print results
# print("Sequence:", sequence)
# print("Sequence * (1/9) = ", [round(x * (1/9), 3) for x in sequence])
# '''
# https://oeis.org/A285396 (1/9)

# remainder counted as integers:
# 0 2 0 1 0 0 0 2 0 1 0 0 0 0
# https://oeis.org/A265245

# 0 2 0 1 0 0 0 2 0 1 0 0 0 (breaks after 13)
# https://oeis.org/A110270 <--- super interesting
# related https://oeis.org/A248034



# https://oeis.org/A284825

# '''
# print("Means between terms:", means)
# print("Ratios between terms:", ratios)

# # Check each consecutive set of 3 numbers in ratios to see if they form a triangle
# triangles = []
# for i in range(len(ratios) - 2):
#     a, b, c = ratios[i], ratios[i + 1], ratios[i + 2]
#     if can_form_triangle(a, b, c):
#         angles = calculate_angles(a, b, c)
#         triangles.append((a, b, c, angles))

# # Print the triangles and their angles
# for i, (a, b, c, angles) in enumerate(triangles):
#     print(f"Triangle {i + 1}: sides = ({a:.2f}, {b:.2f}, {c:.2f}), angles = ({angles[0]:.5f}°, {angles[1]:.5f}°, {angles[2]:.5f}°)")

# # Plot only the ratios
# plt.figure(figsize=(10, 6))
# plt.plot(ratios, marker='s', linestyle='-.', color='g', label='Ratios between terms')
# plt.title('Ratios between Consecutive Terms')
# plt.xlabel('Index')
# plt.ylabel('Ratio')
# plt.legend()
# plt.grid(True)
# plt.show()

import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Convert the binary sequence into a numerical array
binary_sequence = "10101110101110001000110010111111101001110111001010010001101"
binary_array = np.array([int(bit) for bit in binary_sequence])

# Plot the original binary sequence
plt.figure(figsize=(12, 4))
plt.plot(binary_array, marker='o', linestyle='-', color='b')
plt.title("Original Binary Sequence", fontsize=14)
plt.xlabel("Index", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.grid(True)
plt.show()

# Perform a Fast Fourier Transform (FFT)
fft_result = fft(binary_array)
frequencies = np.abs(fft_result)  # Magnitudes of the FFT

# Print all points of the Fourier Transform
print("Fourier Transform Points:")
for i, freq in enumerate(frequencies):
    print(f"Index {i}: {freq}")

# Plot the frequencies to visualize periodicity
plt.figure(figsize=(12, 6))
plt.plot(frequencies[:len(frequencies)//2], marker='o', linestyle='-', color='r')  # Plot only positive frequencies
plt.title("Fourier Transform of the Binary Sequence", fontsize=14)
plt.xlabel("Frequency Index", fontsize=12)
plt.ylabel("Magnitude", fontsize=12)
plt.grid(True)
plt.show()

# Autocorrelation calculation
autocorr = np.correlate(binary_array, binary_array, mode='full')
autocorr = autocorr[len(autocorr)//2:]  # Take only the positive lags

# Print all points of the autocorrelation
print("Autocorrelation Points:")
for i, value in enumerate(autocorr):
    print(f"Lag {i}: {value}")

# Plot the autocorrelation
plt.figure(figsize=(12, 6))
plt.plot(autocorr, marker='o', linestyle='-', color='g')
plt.title("Autocorrelation of the Binary Sequence", fontsize=14)
plt.xlabel("Lag", fontsize=12)
plt.ylabel("Autocorrelation Value", fontsize=12)
plt.grid(True)
plt.show()

# Identify peaks in the autocorrelation function
peaks, _ = find_peaks(autocorr)
print("Peaks in Autocorrelation:", peaks)

# Calculate the distances between consecutive peaks to determine the period
if len(peaks) > 1:
    periods = np.diff(peaks)
    print("Periods from Autocorrelation:", periods)
else:
    print("Not enough peaks to determine periods from autocorrelation.")

# Identify peaks in the Fourier Transform magnitude spectrum
fft_peaks, _ = find_peaks(frequencies[:len(frequencies)//2])
print("Peaks in Fourier Transform:", fft_peaks)

# Calculate the periods from the Fourier Transform peaks
if len(fft_peaks) > 0:
    periods_from_fft = 1 / fft_peaks
    print("Periods from Fourier Transform:", periods_from_fft)
else:
    print("No peaks found in Fourier Transform to determine periods.")