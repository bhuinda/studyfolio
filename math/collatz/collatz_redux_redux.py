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

# clz_frame := tensor storage
clz_frame = []
def clz_f(clz_i, clz_m):
    clz_frame.append([clz_i, clz_m])

# clz := an attempt at realizing a CPT tensor
def clz(i):
    # configuration space
    clz_i,j,k = i,i%2,i
    x,y,z = 0,0,0

    # rotations
    r = 1

    # moments of inertia (i.e., a variation of action)
    clz_v = [((x,y,z),(i,j,k,r))]

    while not (clz_i in (0, 1, 2) and z == 3):
        m,n   = e_f(clz_i)
        x,y,z = x_y_z(x,y,z)
        match z:
            case 0: j,k = m, n
            case 1: j,k = m, n
            case 2: j,k = m,-n
            case 3: j,k = m,-n
        clz_i = n
        r += 1
        clz_v.append(((x,y,z),(i,j,k,r)))

    for a,b in clz_v:
        clz_f(clz_i, (a,b))
    clz_f("␢ħ","␢ħ")

def clz_freq():
    # z_1 := frequency of  steps ~ 1
    # z_2 := frequency of  steps ~ 2
    # s_1 := frequency of |steps| ~ 1
    # s_2 := frequency of |steps| ~ 2
    # p_0 := frequency of i mod 2 ~ 0
    # p_1 := frequency of i mod 2 ~ 1
    z_1,z_2 = 0,0
    s_1,s_2 = 0,0
    p_0,p_1 = 0,0

    last_clz_i = None
    for clz_i, coords in clz_frame:
        if clz_i == "␢ħ":
            
            if   last_clz_i == 1: s_1 += 1
            elif last_clz_i == 2: s_2 += 1
            last_clz_i = None
            continue

        if last_clz_i is not None and last_clz_i != clz_i:
            if   last_clz_i == 1 and clz_i == 2: s_1 += 1
            elif last_clz_i == 2 and clz_i == 1: s_2 += 1

        if   clz_i == 1: z_1 += 1
        elif clz_i == 2: z_2 += 1
        last_clz_i = clz_i
        
        m = coords[1][1]
        if m % 2 == 0: p_0 += 1
        if m % 2 == 1: p_1 += 1

    return s_1,s_2, z_1,z_2, p_0,p_1

# clz analysis
n = 1000; terms = [clz(i) for i in range(1,n + 1)]
s_1,s_2, z_1,z_2, p_0,p_1 = clz_freq()

# save data to file
with open("collatz_data/clz_terms.dat", "w") as file:
    for moment in clz_frame:
        clz_i, coords = moment
        if clz_i == "␢ħ":
            continue
            # file.write("\n")
        else:
            coords_1, coords_2 = coords
            x, y, z = coords_1[0], coords_1[1], coords_1[2]
            i, j, k, r = coords_2[0], coords_2[1], coords_2[2], coords_2[3]
            # file.write(f"{k if not x else j} {k if x else j} {i}\n")     # "WORMHOLE" 
            # file.write(f"{k if x else j} {k if not x else j} {k}\n")     # "ONE SHURIKEN"
            # file.write(f"{k if x else j} {k if not x else j} {clz_i}\n") # "TWO SHURIKEN"
            # file.write(f"{k if x else j} {k if not x else j} {y}\n")     # "ONE BOWTIE"
            # file.write(f"{k if x else j} {k if not x else j} {z}\n")     # "ONE BOWTIE???"
            # file.write(f"{k} {clz_i} {z}\n")                             # "TWO BOWTIE???"
            
            # 2D
            file.write(f"{k if x else j} {k if not x else j} {r}\n")

# clz_i ~ (1,2)

# x(2) ~ (e,i)
# y(2) ~ (+,-)
# z(4) ~ (a,b)

# i(2) ~ (1,2) terminal
# j(2) ~ (0,1) mod
# k(Z) ~ start

# diagnostics
print(f"\nn: {n}\n")
print(f"s_1: {s_1} ~ {s_1 / (s_1 + s_2)}")
print(f"s_2: {s_2} ~ {s_2 / (s_1 + s_2)}\n")
print(f"z_1: {z_1} ~ {z_1 / (z_1 + z_2)}")
print(f"z_2: {z_2} ~ {z_2 / (z_1 + z_2)}\n")
print(f"p_0: {p_0} ~ {p_0 / (p_0 + p_1)}")
print(f"p_1: {p_1} ~ {p_1 / (p_0 + p_1)}")