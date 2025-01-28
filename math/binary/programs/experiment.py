# Given number as a string

""""
90 225 306 495 648 747

https://oeis.org/A206011

90  =     9 + 0 = 9  (ordered)
225 = 2 + 2 + 5 = 9  (commutative)
306 = 3 + 0 + 6 = 9  (associative)
495 = 4 + 9 + 5 = 18 (alternative)
648 = 6 + 4 + 8 = 18 (power associative)
747 = 7 + 4 + 7 = 18 (zero divisors)

900 = 9 + 0 + 0 = 9  (ordered...)

https://oeis.org/search?q=1+2+3+5+7+8+10&go=Search

 90 / 9 = 10
225 / 9 = 25
306 / 9 = 34
495 / 9 = 55
648 / 9 = 72
747 / 9 = 83
900 / 9 = 100

 90 / 90 =  2.0
225 / 45 =  5.0
306 / 45 =  6.8
495 / 45 = 11.0
648 / 45 = 14.4
747 / 45 = 16.6
900 / 45 = 20.0

 90 / 90 = 1.0
225 / 90 = 2.5
306 / 90 = 3.4
495 / 90 = 5.5
648 / 90 = 7.2
747 / 90 = 8.3
900 / 90 = 10.0

1.0, 2.5, 3.4, 5.5, 7.2, 8.3, 10.0

 90 / 90 = 1.0  * 5 =  5.0
225 / 90 = 2.5  * 2 =  5.0
306 / 90 = 3.4  * 5 = 17.0
495 / 90 = 5.5  * 2 = 11.0
648 / 90 = 7.2  * 5 = 36.0
747 / 90 = 8.3  * 2 = 16.6 (THIS BREAKS THE PATTERN. RELATED TO ABEL-RUFFINI THEOREM?)
900 / 90 = 10.0 * 5 = 50.0

 90 / 180 = 0.50 ~ 0 +  1/2 ~   1 pi/2
225 / 180 = 1.25 ~ 1 +  1/4 ~   5 pi/4
306 / 180 = 1.70 ~ 1 + 7/10 ~  17 pi/30
495 / 180 = 2.75 ~ 2 +  3/4 ~  11 pi/4
648 / 180 = 3.60 ~ 3 +  3/5 ~  18 pi/5
747 / 180 = 4.15 ~ 4 + 3/20 ~ 249 pi/60
900 / 180 = 5.00 ~ 5pi
"""

number_str_1 = "393436484784067725"
number_str_2 = "1417693531071288485032644754963173958251807549375"
number_str_3 = "1850921250575100718492138195560502378525160341424138153082390913443908223563775"
number_str_4 = "2348473151348988706257184324579972328534600411767891705739555340824497340345684605543900628253107967242469375"
number_str_5 = "2977128664227288965514153794088930333469831474387218296856433861796749299922558081972602119544120813219351903510329952497361334139644542975"
number_str_6 = "3773962315863473905399616122771731530295254025312173637971661619426778323557060122315571940956527367993460560966220962375513058330079684463164933553748091863386214629375"
number_str_7 = "4784065728747537197180369736437178690095518709780265737462215474382126590343607768609028084898171137666003791029514128457411243291455987392125544333133609085379324503750542642811913297767474739019775"

# import numpy as np
# import matplotlib.pyplot as plt

# # Given numbers for analysis
# numbers = [90, 225, 306, 495, 648, 747]

# # Calculate the mean
# means = np.mean(numbers)

# # Prepare data for plotting
# fig, axs = plt.subplots(2, 3, figsize=(18, 12))

# # Plot 1: The numbers themselves as a bar graph (Row-wise)
# axs[0, 0].bar(range(len(numbers)), numbers, color='skyblue')
# axs[0, 0].set_title('Bar Graph of Numbers (Row-wise)')
# axs[0, 0].set_xticks(range(len(numbers)))
# axs[0, 0].set_xticklabels([str(num) for num in numbers])
# axs[0, 0].set_ylabel('Value')

# # Plot 2: Histogram of the numbers (Row-wise)
# axs[0, 1].hist(numbers, bins=5, color='lightgreen', edgecolor='black')
# axs[0, 1].set_title('Histogram of Numbers (Row-wise)')
# axs[0, 1].set_xlabel('Value')
# axs[0, 1].set_ylabel('Frequency')

# # Plot 3: Line graph of the numbers (Row-wise)
# axs[0, 2].plot(range(len(numbers)), numbers, marker='o', color='orange')
# axs[0, 2].set_title('Line Graph of Numbers (Row-wise)')
# axs[0, 2].set_xticks(range(len(numbers)))
# axs[0, 2].set_xticklabels([str(num) for num in numbers])
# axs[0, 2].set_ylabel('Value')

# # Plot 4: Bar graph for column sums (Sum of digits for each number)
# digits_sums = [sum([int(digit) for digit in str(num)]) for num in numbers]
# axs[1, 0].bar(range(len(numbers)), digits_sums, color='lightcoral')
# axs[1, 0].set_title('Column Sum of Digits (Row-wise)')
# axs[1, 0].set_xticks(range(len(numbers)))
# axs[1, 0].set_xticklabels([str(num) for num in numbers])
# axs[1, 0].set_ylabel('Sum of Digits')

# # Plot 5: Scatter plot of number vs. column sum
# axs[1, 1].scatter(numbers, digits_sums, color='purple')
# axs[1, 1].set_title('Scatter Plot of Numbers vs. Sum of Digits')
# axs[1, 1].set_xlabel('Number')
# axs[1, 1].set_ylabel('Sum of Digits')

# # Plot 6: Pie chart of the column sums (percentage representation)
# axs[1, 2].pie(digits_sums, labels=[str(num) for num in numbers], autopct='%1.1f%%', colors=plt.cm.Paired.colors)
# axs[1, 2].set_title('Pie Chart of Column Sum of Digits')

# # Display the mean of the numbers
# plt.figtext(0.5, 0.01, f'Mean: {means:.2f}', ha='center', fontsize=12)

# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Convert the number strings to integer arrays
def string_to_int_array(num_str):
    return np.array([int(digit) for digit in num_str])

# Define the number strings
number_strs = [
    "393436484784067725",
    "1417693531071288485032644754963173958251807549375",
    "1850921250575100718492138195560502378525160341424138153082390913443908223563775",
    "2348473151348988706257184324579972328534600411767891705739555340824497340345684605543900628253107967242469375",
    "2977128664227288965514153794088930333469831474387218296856433861796749299922558081972602119544120813219351903510329952497361334139644542975",
    "3773962315863473905399616122771731530295254025312173637971661619426778323557060122315571940956527367993460560966220962375513058330079684463164933553748091863386214629375",
    "4784065728747537197180369736437178690095518709780265737462215474382126590343607768609028084898171137666003791029514128457411243291455987392125544333133609085379324503750542642811913297767474739019775",
    "6064523797878659057771094622064210798183202046395698089870529196301771649735057513323646575237802222273449996491593493111982645807965068379136975947814740321035314064413849385207649736625445546045034849471003721266903101133029375"
]

# Compute Fourier transforms for each number string
def compute_fourier_transform(num_str):
    num_array = string_to_int_array(num_str)
    fourier_transform = np.fft.fft(num_array)
    return fourier_transform

# Plot the Fourier transforms (magnitude, phase, real/imag, power spectrum)
fig, axs = plt.subplots(len(number_strs), 5, figsize=(18, len(number_strs)*5))

for i, num_str in enumerate(number_strs):
    # Fourier Transform of the number
    fourier_transform = compute_fourier_transform(num_str)
    
    # Magnitude Spectrum
    magnitude = np.abs(fourier_transform)
    axs[i, 0].plot(magnitude, color='skyblue')
    axs[i, 0].set_title(f'Magnitude Spectrum - Number {i+1}')
    
    # Phase Spectrum
    phase = np.angle(fourier_transform)
    axs[i, 1].plot(phase, color='orange')
    axs[i, 1].set_title(f'Phase Spectrum - Number {i+1}')
    
    # Real Part Spectrum
    real_part = np.real(fourier_transform)
    axs[i, 2].plot(real_part, color='green')
    axs[i, 2].set_title(f'Real Part Spectrum - Number {i+1}')
    
    # Power Spectrum (Magnitude Squared)
    power_spectrum = magnitude ** 2
    axs[i, 3].plot(power_spectrum, color='red')
    axs[i, 3].set_title(f'Power Spectrum - Number {i+1}')
    
    # Log Magnitude Spectrum (logarithmic scaling)
    log_magnitude = np.log10(magnitude + 1e-10)  # Adding a small constant to avoid log(0)
    axs[i, 4].plot(log_magnitude, color='purple')
    axs[i, 4].set_title(f'Log Magnitude Spectrum - Number {i+1}')

# Remove axis labels, numbers (ticks), and legends
for ax in axs.flatten():
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])  # Remove x-ticks
    ax.set_yticks([])  # Remove y-ticks
    ax.legend().set_visible(False)

# Adjust space between subplots vertically
plt.subplots_adjust(hspace=0.5)  # Increase hspace value to add more vertical space

plt.tight_layout()
plt.show()

# Define the number strings
number_strs = [
    "393436484784067725",
    "1417693531071288485032644754963173958251807549375",
    "1850921250575100718492138195560502378525160341424138153082390913443908223563775",
    "2348473151348988706257184324579972328534600411767891705739555340824497340345684605543900628253107967242469375",
    "2977128664227288965514153794088930333469831474387218296856433861796749299922558081972602119544120813219351903510329952497361334139644542975",
    "3773962315863473905399616122771731530295254025312173637971661619426778323557060122315571940956527367993460560966220962375513058330079684463164933553748091863386214629375",
    "4784065728747537197180369736437178690095518709780265737462215474382126590343607768609028084898171137666003791029514128457411243291455987392125544333133609085379324503750542642811913297767474739019775"
]

# Convert each number string to binary and print
for i, num_str in enumerate(number_strs):
    num = int(num_str)
    binary_str = bin(num)[2:]  # Remove the '0b' prefix
    print(f"Binary of Number {i+1}: {binary_str}")
