def repeater(n):
    b = 0.2
    i = 0
    print(f"{i} {b:.3f}")
    while i < n:
        if i % 2 == 0: b += 0.052
        if i % 2 == 1: b += 0.025
        i += 1
        print(f"{i} {b:.3f}")
    return b

repeater(2000)

'''
y = 77/200x + 40/200

y =  0
x = -0.51948051948

y = 0.97
x = 2

y = 1.9976426195 (2)
x = 4.6692016091 (δ)

interesting values:
  0, 0.200
 10, 0.585
 20, 0.970
 30, 1.355
 40, 1.740
 50, 2.125
 60, 2.510
 70, 2.895
 80, 3.280
 90, 3.665
100, 4.050

4.05 * 200/9 = 90

y = 0.97 when x = 2
y = 2.00 when x ~ Feigenbaum constant

difference from y = 2 when x = Feigenbaum constant:
0.00235734895

interestingly, this half-approximates the error of the Feigenbaum constant's
approximation to 10/pi-1

'''