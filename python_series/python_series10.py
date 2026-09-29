N = int(input('Enter N: '))
found = False
for i in range(N):
    x = int(input('Enter number: '))
    if x > 0:
        found = True
if found:
    print('TRUE')
else:
    print('FALSE')
