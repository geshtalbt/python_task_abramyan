a = float(input('enter number: '))
b = float(input('enter number: '))
if a < 0 or b < 0:
    print('Error: Please enter non-negative numbers.')
mean_geometric = (a * b) ** 0.5
print('geometric mean = ', mean_geometric)