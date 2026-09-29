x1 = float(input('enter x1: '))
y1 = float(input('enter y1: '))
x2 = float(input('enter x2: '))
y2 = float(input('enter y2: '))
x3 = float(input('enter x3: '))
y3 = float(input('enter y3: '))
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
c = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
P = a + b + c
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('The area of the triangle is: ', round(S, 2))
print('The perimeter of the triangle is: ', round(P, 2))