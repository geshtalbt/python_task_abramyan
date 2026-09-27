B = float(input('Enter B: '))
N = int(input('Enter N: '))
placed = False
for i in range(N):
    x = float(input('Enter number: '))
    if not placed and B <= x:
        print(B)
        placed = True
    print(x)
if not placed:
    print(B)
