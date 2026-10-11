"""Boolean32. Даны целые числа a, b, c, являющиеся сторонами некоторого тре- угольника. Проверить истинность высказывания: «Треугольник со сторо- нами a, b, c является прямоугольным»."""
a, b, c = map(int, input().split())
condition = max(a,b,c)**2 == (a*a+b*b+c*c-max(a,b,c)**2)
print("TRUE" if condition else "FALSE")
