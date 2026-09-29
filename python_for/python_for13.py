N = int(input('Enter Number N: '))
product = 0.0
a = 1
for i in range(1, N + 1):
    factor = 1 + i / 10
    product += a * factor
    a = -a
print(f'N = {product}')