# a study inspired by insanity, by @bhuinda

# clz := a spicy version of the Collatz pattern
def clz_new(n):
    # pre-processors
    # a := C(2) ~ (e, i) ~ the linear cycle of complexity: (e ⟺ i)
    # b := C(2) ~ (+, -) ~ the linear cycle of polarity: (- ⟺ +)
    # c := C(2) ~ (1, 2) ~ the linear cycle of parity: (-i, -2) -> (+e, +1), (-i, -1) -> (+e, +2)
    a = 0; b = 0; c = n

    # post-processors
    # ab := (a, b) ~ (x, y) ~ the Euclidian 2-space
    # abc := (a, b, c) ~ (x, y, z) ~ the Euclidian 3-space
    ab = []; abc = []

    # p := C(4) ~ (a, b) ~ the square cycle of (e ⟺ i) × (- ⟺ +)
    # q := Z(k) ~ (c, k) ~ the quantity of non-trivial cycles; i.e, the cardinality of p
    p = 0; q = 0

    # nth term
    ab.append((n, 0))

    # nth - i term
    while not (c in (0, 1, 2) and p == 3):
        x, y = 0, 0
        match a, b:
            case 0, 0: a, b, y = 1, 0,  c; p += 1
            case 1, 0: a, b, x = 0, 1, -c; p += 1
            case 0, 1: a, b, y = 1, 1, -c; p += 1
            case 1, 1: a, b, x = 0, 0,  c; p  = 0
        match c % 2:
            case 0: c = (1 * c + 0) // 2
            case 1: c = (3 * c + 1) // 2

        # post-process
        if p == 1: q += 1
        
        # 2-space map
        ab.append((x, y))

    # 3-space map
    for (x, y) in ab: abc.append((x, y, c))
    
    # string terminator
    abc.append('␢ħ')
    
    return abc, c

# clz analysis

# a series of clz terms (k in Z : k ≥ 0)
k = 20; terms = [clz_new(i) for i in range(0, k + 1)]

# s_1 := frequency of e on Z(1) 
# s_2 := frequency of e on Z(2)
# z_1 := frequency of d on C(2, 1)
# z_2 := frequency of d on C(2, 2)
s_1 = 0
s_2 = 0
z_1 = 0
z_2 = 0

# frequency counter
for abc, c in terms:
    match c:
        case 1: s_1 += 1
        case 2: s_2 += 1
    for coord in abc:
        if coord == '␢ħ': break
        match coord[2]:
            case 1: z_1 += 1
            case 2: z_2 += 1

# terminal info
print(f'\non k: {k}\n')
print(f'Z(1): {z_1} ~ {z_1 / (z_1 + z_2)}')
print(f'Z(2): {z_2} ~ {z_2 / (z_1 + z_2)}')
print(f'S(1): {s_1} ~ {s_1 / (s_1 + s_2)}')
print(f'S(2): {s_2} ~ {s_2 / (s_1 + s_2)}')

# save calculation for graphical analysis
with open("collatz_data/data.dat", "w") as file:
    for abc, _ in terms:
        for coord in abc:
            if coord == '␢ħ': file.write("\n")
            else: file.write(f"{coord[0]} {coord[1]} {coord[2]}\n")