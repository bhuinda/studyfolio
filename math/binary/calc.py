import math

GOLDEN_ANGLE = 90.04145414831363

x_0 = 0.5 # 11 / 00
x_1 = 9.0 # 1001
x_2 = 195.0 # 11000011
x_3 = 3591.0 # 111000000111
x_4 = 61455.0 # 1111000000001111
x_5 = 1015839.0 # 11111000000000011111

# r_g = math.log(x_0 * x_1 * x_2 * x_3 * x_4 * x_5) * math.sqrt(5) + 1.0
r_g = GOLDEN_ANGLE

def golden_module(n, i):
    # rotation vars
    r_i = 0 # step
    r_j = 0 # sign
    r_k = 0 # angle

    while r_i < i:
        r_i += 1
        r_j =~ r_j
        r_k += r_g
        print(r_i, r_j, r_k)
    
    return r_k

# for i = 3, ceiling applies to integer right of decimal
# for i = 12, ceiling applies to integer left of decimal

# i = 8; decimal ratio ~ 1/3
# i = 12; decimal ratio ~ 1/2
# i = 16; decimal ratio ~ 2/3
# i = 24; decimal ratio ~ 3/3
print(golden_module(0, 5))