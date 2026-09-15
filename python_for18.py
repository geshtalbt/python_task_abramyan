A = float(input('Enter A: '))
N = int(input('Enter N: '))
a = 1
power = 1
sum = 1
for i in range(1, N+1):
    power *= A
    a = -a
    sum += a * power
print(sum)
