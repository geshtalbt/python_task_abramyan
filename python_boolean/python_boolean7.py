"""Boolean7*. Даны три целых числа: A, B, C. Проверить истинность высказы- вания: «Число B находится между числами A и C»."""
A, B, C = map(int, input().split())
condition = min(A,C) < B < max(A,C)
print("TRUE" if condition else "FALSE")
