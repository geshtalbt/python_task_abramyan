P = float(input('Enter P: '))
day = 10.0
total = 0.0
K = 0
while total <= 200:
    total += day
    K += 1
    day += day * P / 100
print(K)
print(total)
