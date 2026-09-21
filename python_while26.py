N = int(input('Enter N: '))
a = 1
b = 1
while b < N:
    a, b = b, a + b
prev = a
nxt = a + b
print(prev)
print(nxt)
