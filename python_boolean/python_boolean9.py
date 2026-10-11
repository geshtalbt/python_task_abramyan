"""Boolean9. Даны два целых числа: A, B. Проверить истинность высказывания: «Хотя бы одно из чисел A и B нечетное». 12 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4"""
A, B = map(int, input().split())
condition = A%2!=0 or B%2!=0
print("TRUE" if condition else "FALSE")
