A = int(input('Enter A: '))
B = int(input('Enter B: '))
C = int(input('Enter C: '))
N = (A // C) * (B // C)
S = A * B - N * C * C
print(N)
print(S)