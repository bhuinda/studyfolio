import re
import numpy as np
import matplotlib.pyplot as plt

# Define the binary strings
binary_strings = [
    "10101110101110001000110010111111101001110111001010010001101",
    "1111100001010011100100111001101001101101110100110001000011001010010000111010111111001011000010011010111010111101001011110001010101100001001010001010011110111111",
    "11111111110000100000010011011000011010110110010100010001010100111111111111100010101100110101010100110011011101011111001010101010110101010100110010001010010110110011000001101010110010101010001011111110111111110001010101010001110110110010100000001111011111111111",
    "111111111111111000010000000000010011011000000000110101110000110111010000111010100110001000000110001011001001001001110000111001010011110100110000110000001000011000010101010101000000000010101010100111100111111000001111001110001100000110101111001010110110110100111001110111111001110000101111000101101111001010001110111111101100101000000000000111101111111111111111",
    "1111111111111111111100001000000000000000010011011000000000000001101011100001111111011101000011101001000010110001000000110010111100110010010010101011100000011100101000100011110010110000110010101101101010110000101010101010000000000000000000010101010100111101010100101011010011110011010011101111100011010111011111001100110110110101001111010011101111110011010000100010111100010110111111111001010001110111111111111011001010000000000000000011110111111111111111111111",
    "11111111111111111111111110000100000000000000000000010011011000000000000000000011010111000011111111111101110100001110100100000000010110001000000110010111111111001100100100101010111111110000001110010100010000100010110010110000110010110010110101010101100001010101010100000000000000000000000000000010101010100111101010101010110100110100111100110100110100001111110001101011101111100000001100110110110101001111111110100111011111100110100000000010001011110001011011111111111111001010001110111111111111111110110010100000000000000000000001111011111111111111111111111111",
    "111111111111111111111111111111000010000000000000000000000000010011011000000000000000000000000110101110000111111111111111110111010000111010010000000000000010110001000000110010111111111111110011001001001010101111111111111000000111001010001000010000000010110010110000110010110010111111101010101011000010101010101000000000000000000000000000000000000000010101010100111101010101010111111101001101001111001101001101000000000111111000110101110111110000000000001100110110110101001111111111111101001110111111001101000000000000001000101111000101101111111111111111111001010001110111111111111111111111101100101000000000000000000000000000111101111111111111111111111111111111"
]

import re
import matplotlib.pyplot as plt
import numpy as np

# Binary strings for analysis
binary_strings = [
    "10101110101110001000110010111111101001110111001010010001101",
    "1111100001010011100100111001101001101101110100110001000011001010010000111010111111001011000010011010111010111101001011110001010101100001001010001010011110111111",
    "11111111110000100000010011011000011010110110010100010001010100111111111111100010101100110101010100110011011101011111001010101010110101010100110010001010010110110011000001101010110010101010001011111110111111110001010101010001110110110010100000001111011111111111",
    "111111111111111000010000000000010011011000000000110101110000110111010000111010100110001000000110001011001001001001110000111001010011110100110000110000001000011000010101010101000000000010101010100111100111111000001111001110001100000110101111001010110110110100111001110111111001110000101111000101101111001010001110111111101100101000000000000111101111111111111111",
    "1111111111111111111100001000000000000000010011011000000000000001101011100001111111011101000011101001000010110001000000110010111100110010010010101011100000011100101000100011110010110000110010101101101010110000101010101010000000000000000000010101010100111101010100101011010011110011010011101111100011010111011111001100110110110101001111010011101111110011010000100010111100010110111111111001010001110111111111111011001010000000000000001111011111111111111111111",
    "11111111111111111111111110000100000000000000000000010011011000000000000000000011010111000011111111111101110100001110100100000000010110001000000110010111111111001100100100101010111111110000001110010100010000100010110010110000110010110010110101010101100001010101010100000000000000000000000000000010101010100111101010101010110100110100111100110100110100001111110001101011101111100000001100110110110101001111111110100111011111100110100000000010001011110001011011111111111111001010001110111111111111111110110010100000000000000000000001111011111111111111111111111111",
    "111111111111111111111111111111000010000000000000000000000000010011011000000000000000000000000110101110000111111111111111110111010000111010010000000000000010110001000000110010111111111111110011001001001010101111111111111000000111001010001000010000000010110010110000110010110010111111101010101011000010101010101000000000000000000000000000000000000000010101010100111101010101010111111101001101001111001101001101000000000111111000110101110111110000000000001100110110110101001111111111111101001110111111001101000000000000001000101111000101101111111111111111111001010001110111111111111111111111101100101000000000000000000000000000111101111111111111111111111111111111"
]

# Function to analyze binary string
def analyze_binary(binary_str):
    # Analyze lengths of consecutive 1s and 0s
    ones_lengths = [len(match) for match in re.findall('1+', binary_str)]
    zeros_lengths = [len(match) for match in re.findall('0+', binary_str)]

    # Count transitions (from 0 to 1 or 1 to 0)
    transitions = sum(1 for i in range(1, len(binary_str)) if binary_str[i] != binary_str[i-1])

    # Count the number of 1s and 0s
    ones_count = binary_str.count('1')
    zeros_count = binary_str.count('0')

    # Calculate means
    mean_ones_length = np.mean(ones_lengths) if ones_lengths else 0
    mean_zeros_length = np.mean(zeros_lengths) if zeros_lengths else 0

    return {
        'ones_lengths': ones_lengths,
        'zeros_lengths': zeros_lengths,
        'transitions': transitions,
        'ones_count': ones_count,
        'zeros_count': zeros_count,
        'mean_ones_length': mean_ones_length,
        'mean_zeros_length': mean_zeros_length,
    }

# Analyze each binary string
analysis_results = [analyze_binary(binary_str) for binary_str in binary_strings]

# Function to plot the analysis results
def plot_analysis(analysis_results):
    fig, axs = plt.subplots(len(analysis_results), 2, figsize=(18, len(analysis_results) * 5))

    for i, result in enumerate(analysis_results):
        # Plot lengths of 1's
        axs[i, 0].bar(range(len(result['ones_lengths'])), result['ones_lengths'], color='skyblue', label='1s')
        axs[i, 0].set_title(f'Lengths of Consecutive 1s - Binary {i+1}')
        axs[i, 0].set_xticks([])
        axs[i, 0].set_yticks([])

        # Plot lengths of 0's
        axs[i, 1].bar(range(len(result['zeros_lengths'])), result['zeros_lengths'], color='orange', label='0s')
        axs[i, 1].set_title(f'Lengths of Consecutive 0s - Binary {i+1}')
        axs[i, 1].set_xticks([])
        axs[i, 1].set_yticks([])

    plt.tight_layout()
    plt.show()

# Plot the analysis
plot_analysis(analysis_results)

# Function to calculate differences between binary strings
def calculate_differences(binary_strings):
    differences = []
    for i in range(1, len(binary_strings)):
        diff = abs(len(binary_strings[i]) - len(binary_strings[i-1]))
        differences.append(diff)
    return differences

# Print the differences
differences = calculate_differences(binary_strings)
print("Differences in lengths between consecutive binary strings:", differences)

# Print the analysis results
for i, result in enumerate(analysis_results):
    print(f"Binary {i+1}:")
    print(f"  1's Count = {result['ones_count']}, Mean Length of 1's = {result['mean_ones_length']:.2f}")
    print(f"  0's Count = {result['zeros_count']}, Mean Length of 0's = {result['mean_zeros_length']:.2f}")
    print(f"  Transitions = {result['transitions']}")
