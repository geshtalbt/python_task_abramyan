A = float(input('Enter A: '))
k = 0
total = 0.0
while total + 1 / (k + 1) < A:
    k += 1
    total += 1 / k
print(k)
print(total)