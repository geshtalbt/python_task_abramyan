"""Boolean33. Даны целые числа a, b, c. Проверить истинность высказывания: «Существует треугольник со сторонами a, b, c»."""
a, b, c = map(int, input().split())
condition = a+b>c and a+c>b and b+c>a
print("TRUE" if condition else "FALSE")
