N = int(input('Enter N: '))

while N % 3 == 0:
    N //= 3

if N == 1:
    print('TRUE')
else:
    print('FALSE')
