A = float(input('Enter A: '))
B = float(input('Enter B: '))

count = 0

while A>=B:
    A -= B
    count += 1

print(f'the number of segments B lying on segment A: {count}')