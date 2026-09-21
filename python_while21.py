N = int(input('Enter N: '))
n = N
found = False
while n > 0:
    if n % 10 % 2 == 1:
        found = True
    n //= 10
if found:
    print('TRUE')
else:
    print('FALSE')
