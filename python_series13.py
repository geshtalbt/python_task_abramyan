sum = 0
x = int(input('Enter number: '))
while x != 0:
    if x > 0 and x % 2 == 0:
        sum += x
    x = int(input('Enter number: '))
print(sum)
