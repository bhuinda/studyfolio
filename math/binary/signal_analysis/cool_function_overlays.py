import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

# Function to compute and store FFT data for each step
def analyze_fft(binary_pattern, i, l_magnitudes, l_phases, l_r_parts, l_i_parts):
    # Convert binary string to numerical values (1s and 0s)
    signal = np.array([int(digit) for digit in binary_pattern], dtype=float)

    # Compute the FFT of the signal
    fft_result = np.fft.fft(signal)

    # Get the magnitude, phase, real part, and imaginary part
    magnitude = np.abs(fft_result)
    phase = np.angle(fft_result)
    r_part = np.real(fft_result)
    i_part = np.imag(fft_result)

    # Append the results to the respective lists for animation
    l_magnitudes.append(magnitude)
    l_phases.append(phase)
    l_r_parts.append(r_part)
    l_i_parts.append(i_part)

# Function to generate and save FFT animations for different components
def graph_fft(magnitudes, phases, r_parts, i_parts):
    # Create GIF for FFT Magnitude Spectrum
    fig, ax = plt.subplots(figsize=(10, 6))
    # def update_magnitude(i):
    #     ax.clear()
    #     # Plot all magnitudes up to the current step
    #     for j in range(i + 1):
    #         ax.plot(magnitudes[j], label=f'Step {j+1}')
    #         ax.plot(-magnitudes[j][::-1], linestyle='--', label=f'Negative Reflection {j+1}')
    #     ax.set_title('FFT Magnitude Spectrum')
    #     ax.set_xlabel('Frequency')
    #     ax.set_ylabel('Magnitude')
    #     ax.grid(True)
    # ani_magnitude = FuncAnimation(fig, update_magnitude, frames=range(len(magnitudes)), repeat=False)
    # ani_magnitude.save('fft_magnitude_spectrum.gif', writer=PillowWriter(fps=9))
    # plt.close(fig)

    # Create GIF for FFT Phase Spectrum
    fig, ax = plt.subplots(figsize=(10, 6))
    def update_phase(i):
        ax.clear()
        # Plot all phases up to the current step with unwrapping
        for j in range(i + 1):
            # Unwrap the phase
            unwrapped_phase = np.unwrap(phases[j])
            # Normalize by subtracting the first phase value
            normalized_unwrapped_phase = unwrapped_phase - unwrapped_phase[0]
            ax.plot(normalized_unwrapped_phase, label=f'Step {j+1}')
            # ax.plot(-normalized_unwrapped_phase[::-1], linestyle='--', label=f'Negative Reflection {j+1}')

    # def update_phase(i):
    #     ax.clear()
    #     # Plot all phases up to the current step (no unwrapping)
    #     for j in range(i + 1):
    #         # Keep the phase within the range [-π, π]
    #         wrapped_phase = np.angle(np.fft.fft(phases[j]))  # Using np.angle to get the phase directly from the FFT result
    #         ax.plot(wrapped_phase, label=f'Step {j+1}')
    #         # ax.plot(-wrapped_phase[::-1], linestyle='--', label=f'Negative Reflection {j+1}')

    #     ax.set_title('Wrapped FFT Phase Spectrum')
    #     ax.set_xlabel('Frequency')
    #     ax.set_ylabel('Phase (radians)')
    #     ax.grid(True)
    ani_phase = FuncAnimation(fig, update_phase, frames=range(len(phases)), repeat=False)
    ani_phase.save('fft_phase_spectrum.gif', writer=PillowWriter(fps=4))
    plt.close(fig)

    # Create GIF for FFT Real Part
    # fig, ax = plt.subplots(figsize=(10, 6))
    # def update_real_part(i):
    #     ax.clear()
    #     ax.plot(r_parts[i], label=f'Step {i+1}')
    #     ax.plot(-r_parts[i][::-1], linestyle='--', label=f'Negative Reflection {i+1}')
    #     ax.set_title('FFT Real Part')
    #     ax.set_xlabel('Frequency')
    #     ax.set_ylabel('Real Part')
    #     ax.grid(True)
    # ani_real_part = FuncAnimation(fig, update_real_part, frames=range(len(r_parts)), repeat=False)
    # ani_real_part.save('fft_real_part.gif', writer=PillowWriter(fps=9))
    # plt.close(fig)

    # Create GIF for FFT Imaginary Part
    # fig, ax = plt.subplots(figsize=(10, 6))
    # def update_imaginary_part(i):
    #     ax.clear()
    #     # Plot all imaginary parts up to the current step
    #     for j in range(i + 1):
    #         ax.plot(i_parts[j], label=f'Step {j+1}')
    #         ax.plot(-i_parts[j][::-1], linestyle='--', label=f'Negative Reflection {j+1}')
    #     ax.set_title('FFT Imaginary Part')
    #     ax.set_xlabel('Frequency')
    #     ax.set_ylabel('Imaginary Part')
    #     ax.grid(True)
    # ani_imaginary_part = FuncAnimation(fig, update_imaginary_part, frames=range(len(i_parts)), repeat=False)
    # ani_imaginary_part.save('fft_imaginary_part.gif', writer=PillowWriter(fps=9))
    # plt.close(fig)

# Function to generate binary patterns and compute their FFT data
def digital_pattern(n):
    l_magnitudes = []
    l_phases = []
    l_r_parts = []
    l_i_parts = []

    # Generate binary patterns for n steps and compute FFT for each
    for i in range(1, n * 5 + 1):
        # Create a binary pattern based on the current step
        binary_pattern = f"{'1'*i}{'0'*(i*2)}{'1'*i}"
        analyze_fft(binary_pattern, i, l_magnitudes, l_phases, l_r_parts, l_i_parts)

    # Generate the GIFs using the calculated FFT data
    graph_fft(l_magnitudes, l_phases, l_r_parts, l_i_parts)

# Example usage: Generate FFT data and save GIFs for 4 steps
digital_pattern(18)
