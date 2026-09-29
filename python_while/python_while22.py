N = int(input('Enter N: '))
d = 2
prime = True
while d * d <= N:
    if N % d == 0:
        prime = False
    d += 1
if prime:
    print('TRUE')
else:
    print('FALSE')
