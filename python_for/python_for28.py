X = float(input('Enter X: '))
N = int(input('Enter N: '))
sum = 1
term = 1
for i in range(1, N + 1):
    term *= -X * (2 * i - 3) / (2 * i)
    sum += term
print(sum)