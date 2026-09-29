A = float(input('Enter A: '))
N = int(input('Enter N :'))
stepen = 1
sum = 1
for i in range(1, N+1):
    stepen *= A
    sum += stepen
print(sum)