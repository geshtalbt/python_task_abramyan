N = int(input('Enter N: '))
a = 1
b = 1
while b < N:
    a, b = b, a + b
if b == N or a == N:
    print('TRUE')
else:
    print('FALSE')
