import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def g_product(start, end):
    e_terms = [(4 * 4**n - 2**n)**2 - (2**n - 1)**2 for n in range(start, end + 1)]
    e_logs  = [math.log(e) for e in e_terms]
    e_full  = sum(e_logs)
    e_half  = math.log(1/2)
    i_sqrt  = math.sqrt(5 + (math.pi**4 / 900))
    
    return (e_half + e_full) * i_sqrt

def g_period(n):
    periods = []
    for i in range(n):
        start = i     * 5
        end   = start + 4

        period = g_product(start, end)
        periods.append(period)

        print(f"π/2 ({start} to {end}): {period:.5f}")

    return periods

def plot_natural_logs(pi_values):
    natural_logs = np.log(pi_values)

    plt.figure(figsize=(12, 8))
    plt.plot(range(len(natural_logs)), natural_logs, marker='o', linestyle='-', color='b', label='Natural Logarithms')

    slope, intercept, r_value, p_value, std_err = linregress(range(len(natural_logs)), natural_logs)
    plt.plot(range(len(natural_logs)), intercept + slope * np.array(range(len(natural_logs))), 'r', label='Trend Line')

    window_size = 5
    moving_avg = np.convolve(natural_logs, np.ones(window_size)/window_size, mode='valid')
    plt.plot(range(window_size-1, len(natural_logs)), moving_avg, 'g', label='Moving Average')

    plt.title('Natural Logarithms of π Terms with Trend Line and Moving Average')
    plt.xlabel('Index')
    plt.ylabel('Natural Log Value')
    plt.grid(True)
    plt.legend()
    plt.show()

    return natural_logs

def plot_histogram(pi_values):
    plt.figure(figsize=(8, 6))
    plt.hist(pi_values, bins=20, color='c', edgecolor='k', alpha=0.7)
    plt.title('Histogram of π Values')
    plt.xlabel('π Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_derivative(pi_values):
    derivative = np.diff(pi_values)
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(pi_values)), derivative, marker='o', linestyle='-', color='m', label='Derivative')
    plt.title('Derivative of π Values')
    plt.xlabel('Index')
    plt.ylabel('Derivative')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_cumulative_sum(pi_values):
    cumulative_sum = np.cumsum(pi_values)
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(pi_values)), cumulative_sum, marker='o', linestyle='-', color='y', label='Cumulative Sum')
    plt.title('Cumulative Sum of π Values')
    plt.xlabel('Index')
    plt.ylabel('Cumulative Sum')
    plt.grid(True)
    plt.legend()
    plt.show()

def plot_box_plot(pi_values):
    plt.figure(figsize=(8, 6))
    plt.boxplot(pi_values, vert=False)
    plt.title('Box Plot of π Values')
    plt.xlabel('π Value')
    plt.grid(True)
    plt.show()

def main():
    periods = 300
    print("Generating results for π/2 terms...")
    pi_values = g_period(periods)

    plot_natural_logs(pi_values)
    plot_histogram(pi_values)
    plot_derivative(pi_values)
    plot_cumulative_sum(pi_values)
    plot_box_plot(pi_values)

if __name__ == "__main__":
    main()