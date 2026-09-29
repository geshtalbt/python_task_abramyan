eps = float(input('Enter eps: '))
a1 = 1.0
a2 = 2.0
k = 2
while abs(a2 - a1) >= eps:
    a3 = (a1 + 2 * a2) / 3
    a1 = a2
    a2 = a3
    k += 1
print(k)
print(a1)
print(a2)
