pi = 3.14
a = float(input("Enter a: "))
if a <= 0 or a >= 2*pi:
    print("Error: a must be in the range [0, 2*pi]")
else:
    randian = pi * a / 180
    print(f"randian = {randian}")