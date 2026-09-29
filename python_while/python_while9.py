N = int(input('Enter N: '))

k = 0
power = 1

while power <= N:
    power *= 3
    k += 1

print(k)