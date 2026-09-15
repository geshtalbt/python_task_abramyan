count = 0
A = int(input('Enter Number A: '))
B = int(input('Enter Number B: '))
for i in range(B, A-1, -1):
    print(i)
    count +=1
print(f'Count of numbers: {count}')