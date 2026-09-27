K = int(input('Enter K: '))
i = 0
pos = 0
x = int(input('Enter number: '))
while x != 0:
    i += 1
    if x > K and pos == 0:
        pos = i
    x = int(input('Enter number: '))
print(pos)
