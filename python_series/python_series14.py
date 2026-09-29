K = int(input('Enter K: '))
count = 0
x = int(input('Enter number: '))
while x != 0:
    if x < K:
        count += 1
    x = int(input('Enter number: '))
print(count)
