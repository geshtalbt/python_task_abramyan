A = float(input('Enter A: '))
B = float(input('Enter B: '))
C = float(input('Enter C: '))
restA = A
nx = 0
while restA >= C:
    restA -= C
    nx += 1
restB = B
ny = 0
while restB >= C:
    restB -= C
    ny += 1
count = 0
i = 0
while i < ny:
    count += nx
    i += 1
print(count)
