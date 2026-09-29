N = int(input('Enter N: '))
count = 0
for i in range(N):
    x = int(input('Enter number: '))
    if x % 2 == 0:
        print(x)
        count += 1
print(count)
