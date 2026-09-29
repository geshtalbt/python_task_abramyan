K = int(input('Enter K from 1 to 365: '))
N = int(input('Enter N from 1 to 7: '))
a = (K + N - 2) % 7 + 1
print(a)