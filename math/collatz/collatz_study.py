# a study inspired by insanity, by @bhuinda

# clz := a spicy version of the Collatz pattern
def clz(n):
    # pre-processors
    # a := C(2) ~ (e, i) ~ the linear cycle of parity: (e ⟺ i)
    # b := C(2) ~ (+, -) ~ the linear cycle of polarity: (- ⟺ +)
    # c := C(4) ~ (a, b) ~ the square cycle of (e ⟺ i) × (- ⟺ +)
    # d := C(2) ~ (1, 2) ~ the physical binary: (-i, 2) -> 1, (-i, 1) -> 2
    # e := Z(k) ~ (n, c) ~ the quantity of non-trivial cycles; i.e, the cardinality of steps
    a = 0; b = 0; c = 0; d = n; e = 1

    # post-processors
    # ab := (a, b) ~ (x, y) ~ the Euclidian 2-space
    # abd := (a, b, d) ~ (x, y, z) ~ the Euclidian 3-space
    ab = []; abd = []; x = 0; y = 0

    # nth term
    ab.append((n, 0))

    # nth - k term
    while True:
        if c == 3 and d in (0,1,2): break
        else:
            match a:
                case 0:
                    if b: a = 1; b = 1; x = -d
                    else: a = 1; b = 0; x = d
                case 1:
                    if b: a = 0; b = 0; y = -d
                    else: a = 0; b = 1; y = d
            match c == 3:
                case 0: c += 1; e += 0
                case 1: c -= 3; e += 1
            match d % 2:
                case 0: d = (1 * d + 0) // 2
                case 1: d = (3 * d + 1) // 2

        # 2-space map
        ab.append((x, y))

    # 3-space map
    for (x, y) in ab: abd.append((x, y, d))
    
    # string terminator
    abd.append('␢ħ')
    
    return abd, d

# clz analysis

# a series of clz terms (k in Z : k ≥ 0)
k = 1000; terms = [clz(i) for i in range(0, k + 1)]

# s_1 := frequency of e on Z(1) 
# s_2 := frequency of e on Z(2)
# z_1 := frequency of d on C(2, 1)
# z_2 := frequency of d on C(2, 2)
s_1 = 0
s_2 = 0
z_1 = 0
z_2 = 0

# frequency counter
for abd, d in terms:
    for coord in abd:
        if coord == '␢ħ': break
        match coord[2]:
            case 1: z_1 += 1
            case 2: z_2 += 1
    match d:
        case 1: s_1 += 1
        case 2: s_2 += 1

# terminal info
print(f'\non k: {k}\n')
print(f'Z(1): {z_1} ~ {z_1 / (z_1 + z_2)}')
print(f'Z(2): {z_2} ~ {z_2 / (z_1 + z_2)}')
print(f'S(1): {s_1} ~ {s_1 / (s_1 + s_2)}')
print(f'S(2): {s_2} ~ {s_2 / (s_1 + s_2)}')

# save calculation for graphical analysis
with open("collatz_data/data.dat", "w") as file:
    for abd, _ in terms:
        for coord in abd:
            if coord == '␢ħ': file.write("\n")
            else: file.write(f"{coord[0]} {coord[1]} {coord[2]}\n")