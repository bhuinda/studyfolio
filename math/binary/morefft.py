import numpy as np
import matplotlib.pyplot as plt

# Fourier coefficients (magnitude) from each step (simulated for the example)
step_56_magnitudes = np.abs(np.fft.fft([1.01, 0.01, 1.02, -0.02, 0.98, 1.0, 1.0, 0.02, 1.02, -0.02, 0.98, 1.0, 1.0, 0.03, 0.01, -0.02, 0.99, -0.01, 0.01, 0.03, 1.0, 0.98, -0.01, -0.01, 1.02, 0.02, 0.99, 0.99, 0.98, 0.99, 1.03, 1.02, 0.99, -0.01, 0.98, -0.0, 0.03, 1.01, 1.0, 0.99, -0.03, 1.01, 1.02, 1.01, 0.0, -0.02, 0.98, 0.02, 1.02, 0.01, 0.0, 0.97, -0.01, 0.02, 0.01, 1.02, 0.99, -0.03, 1.0]))  
step_57_magnitudes = np.abs(np.fft.fft([1.0, -0.01, 1.01, -0.0, 1.0, 1.01, 0.99, -0.0, 1.01, -0.01, 1.0, 1.0, 0.99, 0.01, 0.0, -0.01, 1.01, -0.0, -0.01, 0.01, 0.99, 1.0, 0.01, -0.01, 1.0, 0.01, 0.99, 1.01, 1.0, 0.99, 1.01, 1.0, 0.99, 0.01, 0.99, -0.0, 0.01, 0.99, 1.0, 1.01, -0.01, 1.01, 1.0, 0.99, 0.01, -0.0, 0.99, 0.01, 0.99, -0.0, 0.01, 0.99, 0.0, 0.01, -0.01, 1.0, 1.0, -0.01, 1.01]))
step_58_magnitudes = np.abs(np.fft.fft([1.0, -0.0, 1.0, -0.0, 1.0, 1.0, 1.0, -0.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, 0.0, -0.0, 1.0, -0.0, -0.0, 0.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, -0.0, 0.0, 1.0, 1.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, -0.0, 0.0, 1.0, 0.0, 0.0, -0.0, 1.0, 1.0, -0.0, 1.0]))
step_59_magnitudes = np.abs(np.fft.fft([1.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0]))

# Plot magnitudes of the Fourier coefficients for each step
plt.figure(figsize=(10, 6))
plt.plot(step_56_magnitudes, label="Step 56", linestyle='-', marker='o')
plt.plot(step_57_magnitudes, label="Step 57", linestyle='-', marker='o')
plt.plot(step_58_magnitudes, label="Step 58", linestyle='-', marker='o')
plt.plot(step_59_magnitudes, label="Step 59", linestyle='-', marker='o')

plt.title("Magnitude of Fourier Coefficients at Different Steps")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.show()

# Reconstructed signals (simulated for the example)
step_56_signal = [1.01, 0.01, 1.02, -0.02, 0.98, 1.0, 1.0, 0.02, 1.02, -0.02, 0.98, 1.0, 1.0, 0.03, 0.01, -0.02, 0.99, -0.01, 0.01, 0.03, 1.0, 0.98, -0.01, -0.01, 1.02, 0.02, 0.99, 0.99, 0.98, 0.99, 1.03, 1.02, 0.99, -0.01, 0.98, -0.0, 0.03, 1.01, 1.0, 0.99, -0.03, 1.01, 1.02, 1.01, 0.0, -0.02, 0.98, 0.02, 1.02, 0.01, 0.0, 0.97, -0.01, 0.02, 0.01, 1.02, 0.99, -0.03, 1.0]
step_57_signal = [1.0, -0.01, 1.01, -0.0, 1.0, 1.01, 0.99, -0.0, 1.01, -0.01, 1.0, 1.0, 0.99, 0.01, 0.0, -0.01, 1.01, -0.0, -0.01, 0.01, 0.99, 1.0, 0.01, -0.01, 1.0, 0.01, 0.99, 1.01, 1.0, 0.99, 1.01, 1.0, 0.99, 0.01, 0.99, -0.0, 0.01, 0.99, 1.0, 1.01, -0.01, 1.01, 1.0, 0.99, 0.01, -0.0, 0.99, 0.01, 0.99, -0.0, 0.01, 0.99, 0.0, 0.01, -0.01, 1.0, 1.0, -0.01, 1.01]
step_58_signal = [1.0, -0.0, 1.0, -0.0, 1.0, 1.0, 1.0, -0.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, 0.0, -0.0, 1.0, -0.0, -0.0, 0.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, -0.0, 0.0, 1.0, 1.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, -0.0, 0.0, 1.0, 0.0, 0.0, -0.0, 1.0, 1.0, -0.0, 1.0]
step_59_signal = [1.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, -0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, -0.0, 1.0, 1.0, 1.0, 0.0, -0.0, 1.0, 0.0, 1.0, 0.0, -0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0]

# Plot the reconstructed signals at each step
plt.figure(figsize=(10, 6))
plt.plot(step_56_signal, label="Step 56", linestyle='-', marker='o')
plt.plot(step_57_signal, label="Step 57", linestyle='-', marker='o')
plt.plot(step_58_signal, label="Step 58", linestyle='-', marker='o')
plt.plot(step_59_signal, label="Step 59", linestyle='-', marker='o')

plt.title("Reconstructed Signal at Different Steps")
plt.xlabel("Index")
plt.ylabel("Signal Value")
plt.legend()
plt.grid(True)
plt.show()

diff_56_57 = np.abs(np.array(step_56_signal) - np.array(step_57_signal))
diff_57_58 = np.abs(np.array(step_57_signal) - np.array(step_58_signal))
diff_58_59 = np.abs(np.array(step_58_signal) - np.array(step_59_signal))

# Plot the differences
plt.figure(figsize=(10, 6))
plt.plot(diff_56_57, label="Difference (Step 56 - Step 57)", linestyle='-', marker='o')
plt.plot(diff_57_58, label="Difference (Step 57 - Step 58)", linestyle='-', marker='o')
plt.plot(diff_58_59, label="Difference (Step 58 - Step 59)", linestyle='-', marker='o')

plt.title("Difference Between Consecutive Steps")
plt.xlabel("Index")
plt.ylabel("Difference")
plt.legend()
plt.grid(True)
plt.show()