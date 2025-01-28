# import numpy as np
# from scipy.fft import fft, ifft
# import matplotlib.pyplot as plt

# # Original binary sequence
# binary_sequence = [int(b) for b in "10101110101110001000110010111111101001110111001010010001101"]

# # Perform Fourier Transform
# fourier_transform = fft(binary_sequence)
# frequencies = np.fft.fftfreq(len(binary_sequence))
# magnitudes = np.abs(fourier_transform)

# # Filter: Retain only top 5 frequencies
# top_n = 32
# indices = np.argsort(magnitudes)[-top_n:]  # Indices of top magnitudes
# filtered_transform = np.zeros_like(fourier_transform)
# filtered_transform[indices] = fourier_transform[indices]  # Retain only top frequencies

# # Reconstruct sequence using Inverse FFT
# reconstructed_sequence = np.real(ifft(filtered_transform))

# # Plot original and reconstructed sequences
# plt.figure(figsize=(12, 6))

# # Original sequence
# plt.subplot(2, 1, 1)
# plt.stem(range(len(binary_sequence)), binary_sequence, basefmt=" ", linefmt="C0-", markerfmt="C0o")
# plt.title("Original Binary Sequence")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.grid(True)

# # Reconstructed sequence
# plt.subplot(2, 1, 2)
# plt.stem(range(len(reconstructed_sequence)), reconstructed_sequence, basefmt=" ", linefmt="C1-", markerfmt="C1o")
# plt.title(f"Reconstructed Sequence (Top {top_n} Frequencies)")
# plt.xlabel("Index")
# plt.ylabel("Value")
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# import numpy as np
# from scipy.fft import fft, ifft
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation, PillowWriter
# import pandas as pd  # For displaying sequences in a tabular format

# # Original binary sequence
# binary_sequence = [int(b) for b in "10101110101110001000110010111111101001110111001010010001101"]

# # Perform Fourier Transform
# fourier_transform = fft(binary_sequence)
# frequencies = np.fft.fftfreq(len(binary_sequence))
# magnitudes = np.abs(fourier_transform)

# # Set up the figure and axis
# fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# # Plot the original sequence
# axs[0].stem(range(len(binary_sequence)), binary_sequence, basefmt=" ", linefmt="C0-", markerfmt="C0o")
# axs[0].set_title("Original Binary Sequence")
# axs[0].set_xlabel("")
# axs[0].set_ylabel("Value")
# axs[0].grid(True)

# # Initialize the plot for the reconstructed sequence with dummy data
# line = axs[1].stem(range(len(binary_sequence)), np.zeros(len(binary_sequence)), basefmt=" ", linefmt="C1-", markerfmt="C1o")[0]
# axs[1].set_title("Reconstructed Sequence")
# axs[1].set_xlabel("Index")
# axs[1].set_ylabel("Value")
# axs[1].grid(True)

# # List to store recorded sequences for printing
# recorded_sequences = []

# def update(top_n):
#     # Filter: Retain only top_n frequencies
#     indices = np.argsort(magnitudes)[-top_n:]  # Indices of top magnitudes
#     filtered_transform = np.zeros_like(fourier_transform)
#     filtered_transform[indices] = fourier_transform[indices]  # Retain only top frequencies

#     # Reconstruct sequence using Inverse FFT
#     reconstructed_sequence = np.real(ifft(filtered_transform))

#     # Round the reconstructed sequence to 2 decimal places
#     rounded_sequence = [round(val, 4) for val in reconstructed_sequence]
#     recorded_sequences.append(rounded_sequence)

#     # Update the plot
#     line.set_data(range(len(rounded_sequence)), rounded_sequence)
#     axs[1].set_title(f"Reconstructed Sequence (Top {top_n} Frequencies)")
#     return line,

# # Create the animation
# ani = FuncAnimation(fig, update, frames=range(1, len(binary_sequence) + 1), blit=True)

# # Save the animation as a video file
# ani.save('reconstructed_sequence_slow.gif', writer='ffmpeg', fps=0.5)

# plt.show()

# # Create a DataFrame to display recorded sequences in a tabular format
# recorded_df = pd.DataFrame(recorded_sequences, columns=[f"Index {i}" for i in range(len(binary_sequence))])

# # Display the recorded sequences in a nice table format
# print("Recorded Sequences at Each Step (Top N Frequencies):")
# print(recorded_df)

import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Original binary sequence
binary_sequence = [int(b) for b in "10101110101110001000110010111111101001110111001010010001101"]

# Perform Fourier Transform
fourier_transform = fft(binary_sequence)
frequencies = np.fft.fftfreq(len(binary_sequence))
magnitudes = np.abs(fourier_transform)

# Set up the figure and axis
fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# Plot the original sequence
axs[0].stem(range(len(binary_sequence)), binary_sequence, basefmt=" ", linefmt="C0-", markerfmt="C0o")
axs[0].set_title("Original Binary Sequence")
axs[0].set_xlabel("Index")
axs[0].set_ylabel("Value")
axs[0].grid(True)

# Initialize the plot for the reconstructed sequence with dummy data
markerline, stemlines, baseline = axs[1].stem(range(len(binary_sequence)), np.zeros(len(binary_sequence)), basefmt=" ", linefmt="C1-", markerfmt="C1o")
axs[1].set_title("Reconstructed Sequence")
axs[1].set_xlabel("Index")
axs[1].set_ylabel("Value")
axs[1].grid(True)

# List to store recorded sequences for steps 56 through 59
recorded_sequences = []

def update(top_n):
    # Filter: Retain only top_n frequencies
    indices = np.argsort(magnitudes)[-top_n:]  # Indices of top magnitudes
    filtered_transform = np.zeros_like(fourier_transform)
    filtered_transform[indices] = fourier_transform[indices]  # Retain only top frequencies

    # Reconstruct sequence using Inverse FFT
    reconstructed_sequence = np.real(ifft(filtered_transform))

    # Round the reconstructed sequence to 2 decimal places
    rounded_sequence = [round(float(val), 2) for val in reconstructed_sequence]

    # Record only steps 56 through 59
    if 56 <= top_n <= 59:
        recorded_sequences.append(rounded_sequence)

    # Update the plot
    markerline.set_ydata(rounded_sequence)
    stemlines.set_segments(np.array([range(len(rounded_sequence)), rounded_sequence]).T.reshape(-1, 1, 2))
    axs[1].set_title(f"Reconstructed Sequence (Top {top_n} Frequencies)")
    return markerline, stemlines, baseline

# Create the animation
ani = FuncAnimation(fig, update, frames=range(1, len(binary_sequence) + 1), blit=True)

# Save the animation as a video file
ani.save('reconstructed_sequence.gif', writer='ffmpeg', fps=3)

plt.show()

# Print recorded sequences for steps 56 through 59
for idx, seq in enumerate(recorded_sequences, start=56):
    print(f"Step {idx}: {seq}")