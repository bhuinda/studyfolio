import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

def analyze_fft(binary_pattern, i, l_magnitudes, l_phases, l_r_parts, l_i_parts):
    signal = np.array([int(digit) for digit in binary_pattern], dtype=float)

    fft_result = np.fft.fft(signal)

    magnitude = np.abs(fft_result)
    phase = np.angle(fft_result)
    r_part = np.real(fft_result)
    i_part = np.imag(fft_result)

    l_magnitudes.append(magnitude)
    l_phases.append(phase)
    l_r_parts.append(r_part)
    l_i_parts.append(i_part)

def graph_fft(magnitudes, phases, r_parts, i_parts):
    fig, ax = plt.subplots(figsize=(10, 6))
    def update_magnitude(i):
        ax.clear()
        ax.plot(magnitudes[i], label=f'Step {i+1}')
        ax.plot(-magnitudes[i][::-1], linestyle='--', label=f'Negative Reflection {i+1}')
        ax.set_title('FFT Magnitude Spectrum and Negative Reflection')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Magnitude')
        ax.grid(True)
    ani_magnitude = FuncAnimation(fig, update_magnitude, frames=range(len(magnitudes)), repeat=False)
    ani_magnitude.save('fft_magnitude_spectrum.gif', writer=PillowWriter(fps=2))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    def update_phase(i):
        ax.clear()
        ax.plot(phases[i], label=f'Step {i+1}')
        ax.plot(-phases[i][::-1], linestyle='--', label=f'Negative Reflection {i+1}')
        ax.set_title('FFT Phase Spectrum and Negative Reflection')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Phase (radians)')
        ax.grid(True)
    ani_phase = FuncAnimation(fig, update_phase, frames=range(len(phases)), repeat=False)
    ani_phase.save('fft_phase_spectrum.gif', writer=PillowWriter(fps=2))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    def update_real_part(i):
        ax.clear()
        ax.plot(r_parts[i], label=f'Step {i+1}')
        ax.plot(-r_parts[i][::-1], linestyle='--', label=f'Negative Reflection {i+1}')
        ax.set_title('FFT Real Part and Negative Reflection')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Real Part')
        ax.grid(True)
    ani_real_part = FuncAnimation(fig, update_real_part, frames=range(len(r_parts)), repeat=False)
    ani_real_part.save('fft_real_part.gif', writer=PillowWriter(fps=2))
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 6))
    def update_imaginary_part(i):
        ax.clear()
        ax.plot(i_parts[i], label=f'Step {i+1}')
        ax.plot(-i_parts[i][::-1], linestyle='--', label=f'Negative Reflection {i+1}')
        ax.set_title('FFT Imaginary Part and Negative Reflection')
        ax.set_xlabel('Frequency')
        ax.set_ylabel('Imaginary Part')
        ax.grid(True)
    ani_imaginary_part = FuncAnimation(fig, update_imaginary_part, frames=range(len(i_parts)), repeat=False)
    ani_imaginary_part.save('fft_imaginary_part.gif', writer=PillowWriter(fps=2))
    plt.close(fig)

def digital_pattern(n):
    l_magnitudes = []
    l_phases = []
    l_r_parts = []
    l_i_parts = []

    for i in range(1, n * 5 + 1):
        binary_pattern = f"{'1'*i}{'0'*(i*2)}{'1'*i}"
        analyze_fft(binary_pattern, i, l_magnitudes, l_phases, l_r_parts, l_i_parts)

    graph_fft(l_magnitudes, l_phases, l_r_parts, l_i_parts)

digital_pattern(18)
