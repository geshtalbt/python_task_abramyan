a = float(input('enter number: '))
b = float(input('enter number: '))
if a==0 or b==0:
    print('Error: Please enter non-zero numbers.')
minus = a**a - b**b
plus = a**a + b**b
division = a**a / b**b
print('minus = ', minus)
print('plus = ', plus)
print('division = ', division)
