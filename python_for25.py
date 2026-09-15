X = float(input('Enter X: '))
N = int(input('Enter N: '))
sum = 0
power = 1
a = 1
for i in range(1, N + 1):
    power *= X
    sum += a * power / i
    a = -a
print(sum)