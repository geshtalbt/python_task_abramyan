X = float(input('Enter weight(X) in kg: '))
A = float(input('Enter cost: '))
Y = float(input('Enter weight(Y) in kg: '))
price_per_kg = A / X
cost_Y = price_per_kg * Y
print('cost for 1 kg = ', round(price_per_kg, 2))
print(f'cost for {Y} kg = ', round(cost_Y, 2))