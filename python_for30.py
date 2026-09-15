import math
A = float(input('Enter A: '))
B = float(input('Enter B: '))
N = int(input('Enter N: '))
H = (B - A) / N
print(H)
for i in range(N + 1):
    x = A + i * H
    F = 1 - math.sin(x)
    print(F)