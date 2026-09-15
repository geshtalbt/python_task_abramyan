X = float(input("enter X: "))
N = int(input("enter N: "))
sum = X
fact = X
for i in range(1, N + 1):
    fact *= -X * X / ((2 * i) * (2 * i + 1))
    sum += fact
print(sum)