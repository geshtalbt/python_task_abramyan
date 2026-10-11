"""Boolean12. Даны три целых числа: A, B, C. Проверить истинность высказы- вания: «Каждое из чисел A, B, C положительное»."""
A, B, C = map(int, input().split())
condition = A>0 and B>0 and C>0
print("TRUE" if condition else "FALSE")
