V = float(input('Speed of the boat in still water (V): '))
U = float(input('Speed of the river current (U): '))
T1 = float(input('Time taken to travel downstream (T1): '))
T2 = float(input('Time taken to travel upstream (T2): '))
if V < U:
    print("Error: The speed of the boat in still water must be greater than the speed of the river current.")
else:
    S_all = V * T1 + V * T2
    print('The total distance traveled by the boat is: ', round(S_all, 2))
