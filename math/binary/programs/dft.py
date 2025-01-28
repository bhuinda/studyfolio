# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import correlate
# from scipy.fft import fft, fftfreq

# # Generate a sequence with a repeating block of size 2 (dominant period from autocorrelation)
# block_size = 2
# num_repeats = 20  # Length of the sequence

# # Create the repeating sequence
# base_block = [1, 0]  # Example repeating pattern
# generated_sequence = base_block * num_repeats

# # Autocorrelation calculation
# autocorr_result = correlate(generated_sequence, generated_sequence, mode='full')
# lags = np.arange(-len(generated_sequence) + 1, len(generated_sequence))

# # Normalize autocorrelation for plotting
# autocorr_result = autocorr_result / max(autocorr_result)

# # Fourier Transform calculation
# fourier_transform = fft(generated_sequence)
# frequencies = fftfreq(len(generated_sequence))

# # Plot the results
# fig, axs = plt.subplots(2, 1, figsize=(12, 8))

# # Autocorrelation plot
# axs[0].plot(lags, autocorr_result, label="Autocorrelation")
# axs[0].set_title("Autocorrelation of Generated Sequence")
# axs[0].set_xlabel("Lag")
# axs[0].set_ylabel("Normalized Correlation")
# axs[0].legend()
# axs[0].grid(True, linestyle='--', alpha=0.7)

# # Fourier Transform plot
# axs[1].stem(frequencies[:len(frequencies)//2], np.abs(fourier_transform)[:len(frequencies)//2], basefmt=" ", linefmt='C1-', markerfmt='C1o')
# axs[1].set_title("Fourier Transform of Generated Sequence")
# axs[1].set_xlabel("Frequency")
# axs[1].set_ylabel("Magnitude")
# axs[1].grid(True, linestyle='--', alpha=0.7)

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def analyze_fourier_transform(integer):
    # Convert integer to binary sequence
    binary_sequence = bin(integer)[2:]
    binary_array = np.array([int(bit) for bit in binary_sequence])

    # Perform Fourier Transform
    fourier_transform = np.fft.fft(binary_array)
    frequencies = np.fft.fftfreq(len(binary_sequence))
    
    # Magnitude of Fourier Transform
    magnitudes = np.abs(fourier_transform)
    
    # Identify peaks
    peaks = np.argsort(magnitudes)[-10:]  # Top 10 peaks
    dominant_frequencies = frequencies[peaks]
    dominant_magnitudes = magnitudes[peaks]
    
    # Periods from Fourier Transform (1/Frequency, avoid zero frequencies)
    periods = [1/f for f in dominant_frequencies if f != 0]
    
    # Sort by magnitude for better clarity
    sorted_indices = np.argsort(dominant_magnitudes)[::-1]
    dominant_frequencies = dominant_frequencies[sorted_indices]
    dominant_magnitudes = dominant_magnitudes[sorted_indices]
    
    # Ensure valid indices for periods
    periods = np.array(periods)
    valid_indices = sorted_indices[:len(periods)]
    periods = periods[:len(valid_indices)]
    
    # Plot Fourier Transform
    plt.figure(figsize=(10, 6))
    plt.stem(frequencies[:len(frequencies)//2], magnitudes[:len(magnitudes)//2], 
             basefmt=" ", linefmt='C1-', markerfmt='C1o')
    plt.title(f"Fourier Transform of Binary Representation of {integer}")
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    
    # Results
    return {
        "Binary Sequence": binary_sequence,
        "Dominant Frequencies": dominant_frequencies.tolist(),
        "Periods": periods.tolist(),
        "Magnitudes": dominant_magnitudes.tolist()
    }

# Example Usage
integer_value = 393436484784067725  # Replace with your integer
results = analyze_fourier_transform(integer_value)

# Print Results
print("Binary Sequence:", results["Binary Sequence"])
print("Dominant Frequencies:", results["Dominant Frequencies"])
print("Periods:", results["Periods"])
print("Magnitudes:", results["Magnitudes"])