N = int(input('Enter N: '))
prev = None
for i in range(N):
    x = int(input('Enter number: '))
    if x != prev:
        print(x)
    prev = x
