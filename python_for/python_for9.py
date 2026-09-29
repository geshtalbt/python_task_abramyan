A = int(input("Enter A: "))
B = int(input("Enter B: "))
total = 0
for i in range(A, B + 1):
    total += i ** 2
print(f"sum of squares from {A} to {B} = {total}")