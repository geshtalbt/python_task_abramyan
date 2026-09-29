eps = float(input('Enter eps: '))
prev = 2.0
a = 2 + 1 / prev
k = 2
while abs(a - prev) >= eps:
    prev = a
    a = 2 + 1 / prev
    k += 1
print(k)
print(prev)
print(a)
