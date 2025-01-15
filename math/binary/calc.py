import math
from collections import Counter

GOLDEN_ANGLE = 90.04145414831363
PRIMES_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
PRIMES_101_200 = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
PRIMES_201_300 = [211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]
PRIMES_1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

x_0 = 0.5 # 11 / 00
x_1 = 9.0 # 1001
x_2 = 195.0 # 11000011
x_3 = 3591.0 # 111000000111
x_4 = 61455.0 # 1111000000001111
x_5 = 1015839.0 # 11111000000000011111

# r_g = math.log(x_0 * x_1 * x_2 * x_3 * x_4 * x_5) * math.sqrt(5) + 1.0
r_g = GOLDEN_ANGLE

def golden_module(n,i):
    # rotation vars
    r_i = 0 # step
    r_j = 0 # sign
    r_k = 0 # angle

    while r_i < i:
        r_i += 1
        r_j =~ r_j
        r_k += r_g
    
    return r_k

# for i = 3, ceiling applies to integer right of decimal
# for i = 12, ceiling applies to integer left of decimal

# i = 8; decimal ratio ~ 1/3
# i = 12; decimal ratio ~ 1/2
# i = 16; decimal ratio ~ 2/3
# i = 24; decimal ratio ~ 3/3
# print(golden_module(0,12))

data = []
for i in range(0, 10000):
    data.append(golden_module(0,i) % 90)

def count_digit_frequencies_and_parity(floats):
    # Initialize dictionaries for digit counts and parity counts
    digit_count = {str(i): 0 for i in range(10)}
    even_count = 0
    odd_count = 0

    # Define the set of even and odd digits
    even_digits = {'0', '2', '4', '6', '8'}
    odd_digits = {'1', '3', '5', '7', '9'}

    # Iterate over each float in the list
    for num in floats:
        # Convert the number to a string and remove the decimal point
        num_str = str(num).replace('.', '')
        
        # Count each digit and classify it as even or odd
        for char in num_str:
            if char.isdigit():  # Ensure it's a digit
                digit_count[char] += 1
                if char in even_digits:
                    even_count += 1
                elif char in odd_digits:
                    odd_count += 1
    
    return digit_count, even_count, odd_count

# Example usage
floats = data
digit_frequencies, even_digit_count, odd_digit_count = count_digit_frequencies_and_parity(floats)

print("Digit Frequencies:", digit_frequencies)
print("Even Digits Frequency:", even_digit_count)
print("Odd Digits Frequency:", odd_digit_count)