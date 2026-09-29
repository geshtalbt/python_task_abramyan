N = int(input('Enter N: '))
K = int(input('Enter K: '))
sum = 0.0
for i in range(1, N + 1):
    power = 1.0
    for j in range(K):
        power *= i
    sum += power
print(sum)