N = int(input('Enter N: '))

k = 0

while (k + 1) * (k + 1) <= N:
    k += 1

print(k)