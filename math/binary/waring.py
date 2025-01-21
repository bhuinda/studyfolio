import gmpy2
from gmpy2 import mpz, log2, floor

def check_large_k_gmpy2(k):
    # Constants
    ln_three_half = gmpy2.log(3) - gmpy2.log(2)  # ln(3/2)

    # Approximate x_k = (3/2)^k using logarithms
    x_k_log = k * ln_three_half  # ln((3/2)^k)
    fractional_part = x_k_log % 1  # Fractional part of the logarithm
    floor_x_k = gmpy2.floor(gmpy2.exp(fractional_part * gmpy2.log(2)))  # Approximation of floor(x_k)

    # Use modular arithmetic to avoid overflow
    mod = gmpy2.powmod(2, k, 2**k)  # 2^k mod 2^k (stays consistent)
    three_mod = gmpy2.powmod(3, k, 2**k)  # 3^k mod 2^k
    lhs = three_mod - mod * floor_x_k  # LHS of inequality
    rhs = mod - floor_x_k - 2  # RHS of inequality

    # Compare LHS and RHS
    return lhs > rhs

# Example: Evaluate for k = 393436484784067725
k = 393436484784067725
result = check_large_k_gmpy2(k)

print(f"Does the inequality hold for k = {k}? {result}")