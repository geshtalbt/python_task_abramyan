"""Boolean31. Даны целые числа a, b, c, являющиеся сторонами некоторого тре- угольника. Проверить истинность высказывания: «Треугольник со сторо- нами a, b, c является равнобедренным»."""
a, b, c = map(int, input().split())
condition = a==b or b==c or a==c
print("TRUE" if condition else "FALSE")
