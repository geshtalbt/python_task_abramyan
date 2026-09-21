N = int(input('Enter N: '))
a = 1
b = 1
k = 2
while b < N:
    a, b = b, a + b
    k += 1
print(k)
