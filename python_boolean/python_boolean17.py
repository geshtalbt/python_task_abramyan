"""Boolean17. Дано целое положительное число. Проверить истинность выска- зывания: «Данное число является нечетным трехзначным»."""
A, = map(int, input().split())
condition = 100<=A<=999 and A%2!=0
print("TRUE" if condition else "FALSE")
