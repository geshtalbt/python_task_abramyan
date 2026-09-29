pi = 3.14
a = float(input("Enter a: "))
if a <= 0 or a >= 360:
    print("Error: a must be in the range [0, 360]")
else:
    randian = pi * a / 180
    print(f"randian = {randian}")