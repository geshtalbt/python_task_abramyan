"""If13. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим). Условный оператор 15"""
import math
A, B, C = map(float, input().split())
result = sorted((A,B,C))[1]
print(*result if isinstance(result, tuple) else (result,))
