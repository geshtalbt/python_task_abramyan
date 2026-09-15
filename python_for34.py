N = int(input('Enter N: '))
a = 1
b = 2
print(a)
print(b)
for i in range(3, N + 1):
    c = (a + 2 * b) / 3
    print(c)
    a = b
    b = c