"""Boolean8. Даны два целых числа: A, B. Проверить истинность высказывания: «Каждое из чисел A и B нечетное»."""
A, B = map(int, input().split())
condition = A%2!=0 and B%2!=0
print("TRUE" if condition else "FALSE")
