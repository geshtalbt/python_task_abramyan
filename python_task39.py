A = float(input('Enter A number: '))
B = float(input('Enter B number: '))
C = float(input('Enter C number: '))
D = B**2 - 4*A*C
if D > 0:
    x1 = (-B + D**0.5) / (2*A)
    x2 = (-B - D**0.5) / (2*A)
    print(f'The equation {A}x^2 + {B}x + {C} = 0 has two real roots: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}')
elif D == 0:
    x = -B / (2*A)
    print(f'The equation {A}x^2 + {B}x + {C} = 0 has one real root: x = {round(x, 2)}')
else:
    print(f'The equation {A}x^2 + {B}x + {C} = 0 has no real roots.')