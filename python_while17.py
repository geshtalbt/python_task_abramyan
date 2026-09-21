N = int(input('Enter N: '))
n = N
while n > 0:
    digit = n % 10
    print(digit)
    n //= 10
