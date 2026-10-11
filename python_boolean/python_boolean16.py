"""Boolean16. Дано целое положительное число. Проверить истинность выска- зывания: «Данное число является четным двузначным»."""
A, = map(int, input().split())
condition = 10<=A<=99 and A%2==0
print("TRUE" if condition else "FALSE")
