X = float(input('Enter number X: '))
N = int(input('Enter number N: '))
sum = 1
fact = 1
for i in range(1, N+1):
    fact *= X/i
    sum += fact
print(sum)
