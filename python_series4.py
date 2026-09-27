N = int(input('Enter N: '))
sum = 0.0
product = 1.0
for i in range(N):
    x = float(input('Enter number: '))
    sum += x
    product *= x
print(sum)
print(product)
