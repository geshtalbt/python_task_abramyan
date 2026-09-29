A = int(input('Enter A: '))
B = int(input('Enter B: '))
while B != 0:
    A, B = B, A % B
print(A)
