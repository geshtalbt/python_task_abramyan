N = int(input('Enter N: '))
a = 1
b = 2
c = 3
print(a)
print(b)
print(c)
for i in range(4, N + 1):
    d = c + b - 2 * a
    print(d)
    a = b
    b = c
    c = d