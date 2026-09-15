N = int(input('Enter N: '))
sum = 0.0
for i in range(1, N + 1):
    exponent = N - i + 1
    power = 1.0
    for j in range(exponent):
        power *= i
    sum += power
print(sum)