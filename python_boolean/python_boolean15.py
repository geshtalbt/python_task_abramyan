"""Boolean15. Даны три целых числа: A, B, C. Проверить истинность высказы- вания: «Ровно два из чисел A, B, C являются положительными»."""
A, B, C = map(int, input().split())
condition = sum(x>0 for x in (A,B,C))==2
print("TRUE" if condition else "FALSE")
