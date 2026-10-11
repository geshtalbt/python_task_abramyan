"""Boolean10*. Даны два целых числа: A, B. Проверить истинность высказыва- ния: «Ровно одно из чисел A и B нечетное»."""
A, B = map(int, input().split())
condition = (A%2!=0)!=(B%2!=0)
print("TRUE" if condition else "FALSE")
