import math

def digital_function(n):
    result = (30 ** -1) * math.log(n // 2) * math.sqrt(5 * (30 ** 2) + math.pi ** 4)
    return result

def digital_pattern(n):
    product = 1
    for i in range(1, n * 5 + 1):
        binary_pattern = f"{'1'*i}{'0'*(i*2)}{'1'*i}"
        result         = int(binary_pattern, 2)
        product       *= result
        print(f"ln({i}): {math.log(product)}")

        if i % 5 == 0:
            digital_sum        = sum(int(digit) for digit in str(product))
            digital_sum_square = sum(int(digit) for digit in str(digital_sum))

            print(f"ϕ(ln({i})): {digital_function(product)}\n")
            print(f"G({i})^1: {digital_sum}")
            print(f"G({i})^2: {digital_sum_square}\n")

            product = 1

# n := period of 5
n = 18
digital_pattern(n)