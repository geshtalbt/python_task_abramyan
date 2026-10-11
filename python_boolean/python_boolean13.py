"""Boolean13. Даны три целых числа: A, B, C. Проверить истинность высказы- вания: «Хотя бы одно из чисел A, B, C положительное»."""
A, B, C = map(int, input().split())
condition = A>0 or B>0 or C>0
print("TRUE" if condition else "FALSE")
