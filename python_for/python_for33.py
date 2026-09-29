N = int(input('Enter N: '))
a = 1
b = 1
print(a)
print(b)
for i in range(3, N + 1):
    c = a + b
    print(c)
    a = b
    b = c