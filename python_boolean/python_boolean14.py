"""Boolean14. Даны три целых числа: A, B, C. Проверить истинность высказы- вания: «Ровно одно из чисел A, B, C положительное»."""
A, B, C = map(int, input().split())
condition = sum(x>0 for x in (A,B,C))==1
print("TRUE" if condition else "FALSE")
