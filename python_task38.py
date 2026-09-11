A = float(input('Enter A number: '))
B = float(input('Enter B number: '))
if A != 0:
    x = -B / A
    print(f'The solution of the equation {A}x + {B} = 0 is: x = {round(x, 2)}')
else:
    print("Error: A cannot be zero, as it would not be a linear equation.")