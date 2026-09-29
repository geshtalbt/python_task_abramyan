A1 = float(input('Enter A1 number: '))
B1 = float(input('Enter B1 number: '))
A2 = float(input('Enter A2 number: '))
B2 = float(input('Enter B2 number: '))
C1 = float(input('Enter C1 number: '))
C2 = float(input('Enter C2 number: '))
D = A1 * B2 - A2 * B1
x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D
print(f'The solution of the system of equations is: x = {round(x, 2)}, y = {round(y, 2)}')
#finally