N = int(input('Enter N: '))

k = 0
total = 0

while total + (k + 1) <= N:
    k += 1
    total += k

print(k)
print(total)