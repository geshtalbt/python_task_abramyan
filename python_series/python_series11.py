K = int(input('Enter K: '))
N = int(input('Enter N: '))
found = False
for i in range(N):
    x = int(input('Enter number: '))
    if x < K:
        found = True
if found:
    print('TRUE')
else:
    print('FALSE')
