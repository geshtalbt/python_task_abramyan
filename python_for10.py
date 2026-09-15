N = int(input('Enter Number N: '))
total = 0.0
for i in range(1, N + 1):
    total += 1/i
print(f'Sum of 1/i from 1 to {N} = {total}')