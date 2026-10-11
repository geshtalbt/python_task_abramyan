"""Boolean2. Дано целое число A. Проверить истинность высказывания: «Чис- ло A является нечетным»."""
A, = map(int, input().split())
condition = A % 2 != 0
print("TRUE" if condition else "FALSE")
