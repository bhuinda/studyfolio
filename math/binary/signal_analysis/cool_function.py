import numpy as np
import matplotlib.pyplot as plt

def analyze_fft(binary_pattern, i, magnitudes, phases, r_parts, i_parts):
    signal = np.array([int(digit) for digit in binary_pattern], dtype=float)

    fft_result = np.fft.fft(signal)

    # magnitude
    magnitude = np.abs(fft_result)

    # phase
    phase = np.angle(fft_result)
    phase_unwrapped = np.unwrap(phase)

    # real + imaginary
    real_part = np.real(fft_result)
    imaginary_part = np.imag(fft_result)
    
    # overlay lists
    magnitudes.append(magnitude)
    phases.append(phase_unwrapped)
    r_parts.append(real_part)
    i_parts.append(imaginary_part)

def graph_fft(magnitudes, phases, r_parts, i_parts):
    plt.figure(figsize=(10, 6))
    for i, magnitude in enumerate(magnitudes, 1):
        plt.plot(magnitude)
        plt.plot(-magnitude[::-1])
    plt.title('FFT Magnitude Spectrum')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    for i, phase in enumerate(phases, 1):
        plt.plot(phase)
        plt.plot(-phase[::-1])
    plt.title('FFT Phase Spectrum')
    plt.xlabel('Frequency')
    plt.ylabel('Phase (radians)')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    for i, real_part in enumerate(r_parts, 1):
        plt.plot(real_part)
        plt.plot(-real_part[::-1])
    plt.title('FFT Real Part')
    plt.xlabel('Frequency')
    plt.ylabel('Real Part')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    for i, imaginary_part in enumerate(i_parts, 1):
        plt.plot(imaginary_part)
        plt.plot(-imaginary_part[::-1])
    plt.title('FFT Imaginary Part')
    plt.xlabel('Frequency')
    plt.ylabel('Imaginary Part')
    plt.tight_layout()
    plt.show()

def digital_pattern(n):
    l_magnitudes = []
    l_phases = []
    l_r_parts = []
    l_i_parts = []

    for i in range(1, n * 5 + 1):
        binary_pattern = f"{'1'*i}{'0'*(i*2)}{'1'*i}"
        analyze_fft(binary_pattern, i, l_magnitudes, l_phases, l_r_parts, l_i_parts)

    graph_fft(l_magnitudes, l_phases, l_r_parts, l_i_parts)

"""
n := periodicity range. 18 seems... anomalous?
"""
n = 18
digital_pattern(n)