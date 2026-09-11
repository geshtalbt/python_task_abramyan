a = float(input('Enter the length of edge a of the cuboid: '))
b = float(input('Enter the length of edge b of the cuboid: '))
c = float(input('Enter the length of edge c of the cuboid: '))
V = a * b * c
S = 2 * (a * b + a * c + b * c)
print(f'The volume of the cuboid with edges {a}, {b}, and {c} is: ', V)
print(f'The surface area of the cuboid with edges {a}, {b}, and {c} is: ', S)