N = int(input('Enter N: '))
prev = int(input('Enter number: '))
count = 0
for i in range(2, N + 1):
    x = int(input('Enter number: '))
    if prev < x:
        print(prev)
        count += 1
    prev = x
print(count)
