"""Boolean11. Даны два целых числа: A, B. Проверить истинность высказывания: «Числа A и B имеют одинаковую четность»."""
A, B = map(int, input().split())
condition = A%2==B%2
print("TRUE" if condition else "FALSE")
