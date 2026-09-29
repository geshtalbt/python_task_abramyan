N = int(input('Enter number: '))
fact = 1
sum = 1
for i in range(1, N+1):
    fact *= i
    sum += fact
print(sum)