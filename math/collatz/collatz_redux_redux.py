#   f := action
# e,f := Z1 ~ 0
# e,i := C1 ~ 1
def e_f(e_i):
    s_1 = e_i %  2
    s_2 = s_1 *  2
    s_3 = s_2 +  1
    s_4 = s_3 *  e_i
    s_5 = s_4 +  s_1
    s_6 = s_5 // 2
    return s_1,s_6

# a,b := C2(i,e) ~ x
# e,i := C2(-,+) ~ y
#   c := C4(a,b) ~ z
def x_y_z(a,b,c):
    match a,b,c:
        case 0,0,0: x,y,z = 1,0,1
        case 1,0,1: x,y,z = 0,1,2
        case 0,1,2: x,y,z = 1,1,3
        case 1,1,3: x,y,z = 0,0,0
    return x,y,z

# post-processing
clz_frame = []

# abc
def clz_f(clz_i,clz_m):
    clz_frame.append([clz_i,clz_m])

# configuration space
# i := M; clz := L
def clz(i):
    # pre-processors
    clz_i = i
    j,k   = i%2,i
    x,y,z = 0,0,0

    # post-processors
    clz_v = [((x,y,z),(i,j,k))]

    # variation of action
    while not (clz_i in (0,1,2) and z==3):
        m,n = e_f(clz_i)
        x,y,z = x_y_z(x,y,z)
        match z:
            case 0: j,k = m, n
            case 1: j,k = m,-n
            case 2: j,k = m,-n
            case 3: j,k = m, n
        clz_i = n
        clz_v.append(((x,y,z),(i,j,k)))
    
    for a,b in clz_v: clz_f(clz_i,(a,b))

    # sentinel value
    clz_f("␢ħ","␢ħ")

# clz analysis

n = 200; terms = [clz(i) for i in range(1, n + 1)]

# save calculation for graphical analysis
with open("collatz_data/clz_terms.dat", "w") as file:
    for moment in clz_frame:
        clz_i, coords = moment
        if clz_i == "␢ħ": file.write("\n")
        else:
            coords_1, coords_2 = coords
            file.write(f"{clz_i} {coords_2[0]} {coords_2[1]} {coords_2[2]}\n")
            # {coords_1[0]} {coords_1[1]} {coords_1[2]}

# s_1 := frequency of e on Z(1) 
# s_2 := frequency of e on Z(2)
# z_1 := frequency of d on C(2, 1)
# z_2 := frequency of d on C(2, 2)
z_1 = 0; z_2 = 0
s_1 = 0; s_2 = 0
p_0 = 0; p_1 = 0

# note: make this not lazy and dumb later
with open("collatz_data/clz_terms.dat", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            if last_clz_i == 1: s_1 += 1
            else: s_2 += 1
            last_clz_i = None
            continue

        parts = line.split()
        clz_i = int(parts[0]) if parts[0] != '␢ħ' else None

        if clz_i is None: continue

        if clz_i == 1: 
            z_1 += 1
            last_clz_i = 1
        else:
            z_2 += 1
            last_clz_i = 2

        parity = int(parts[3])
        if parity % 2 == 0: p_0 += 1
        else: p_1 += 1

print(f"n: {n}\n")
print(f"s_1 (Cardinality for 1): {s_1} ~ {s_1 / (s_1 + s_2)}")
print(f"s_2 (Cardinality for 2): {s_2} ~ {s_2 / (s_1 + s_2)}\n")
print(f"z_1 (Total count for 1): {z_1} ~ {z_1 / (z_1 + z_2)}")
print(f"z_2 (Total count for 2): {z_2} ~ {z_2 / (z_1 + z_2)}\n")
print(f"p_0 (Count of evens): {p_0} ~ {p_0 / (p_0 + p_1)}")
print(f"p_1 (Count of odds): {p_1} ~ {p_1 / (p_0 + p_1)}")