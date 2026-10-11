"""Boolean1*. Дано целое число A. Проверить истинность высказывания: «Чис- ло A является положительным»."""
A, = map(int, input().split())
condition = A > 0
print("TRUE" if condition else "FALSE")
