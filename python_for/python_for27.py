X = float(input('Enter X: '))
N = int(input('Enter N: '))
sum = X
term = X
for i in range(1, N + 1):
    term *= X * X * (2 * i - 1) ** 2 / ((2 * i) * (2 * i + 1))
    sum += term
print(sum)