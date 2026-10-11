"""Boolean24. Даны числа A, B, C (число A не равно 0). Рассмотрев дискрими- нант D = B2 −4·A·C, проверить истинность высказывания: «Квадратное уравнение A·x2 + B·x + C = 0 имеет вещественные корни»."""
A, B, C = map(int, input().split())
condition = B*B-4*A*C>=0
print("TRUE" if condition else "FALSE")
