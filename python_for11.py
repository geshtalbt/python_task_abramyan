N = int(input('Enter Number N: '))
total = 0
for i in range(N, 2 * N + 1):
    total += i ** 2
print(f'Sum = {total} ')