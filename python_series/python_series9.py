N = int(input('Enter N: '))
count = 0
for i in range(1, N + 1):
    x = int(input('Enter number: '))
    if x % 2 != 0:
        print(i)
        count += 1
print(count)
