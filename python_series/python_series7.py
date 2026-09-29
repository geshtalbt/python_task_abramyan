N = int(input('Enter N: '))
sum = 0
for i in range(N):
    x = float(input('Enter number: '))
    r = round(x)
    print(r)
    sum += r
print(sum)
