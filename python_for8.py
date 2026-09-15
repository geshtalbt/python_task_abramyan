A = int(input("Enter A: "))
B = int(input("Enter B: "))
total = 1
for i in range(A, B + 1):
    total *= i
print(f"Multiply from {A} to {B} = {total}")