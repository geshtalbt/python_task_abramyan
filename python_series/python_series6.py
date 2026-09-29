N = int(input('Enter N: '))
product = 1.0
for i in range(N):
    x = float(input('Enter number: '))
    part = x - int(x)
    print(part)
    product *= part
print(product)
