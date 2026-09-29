N = int(input('Enter N: '))
K = int(input('Enter K: '))

q = 0
r = N

while r >= K:
    r -= K
    q += 1

print(q)
print(r)
