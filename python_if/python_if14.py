"""If14. Даны три числа. Вывести вначале наименьшее, а затем наибольшее из данных чисел."""
import math
A, B, C = map(float, input().split())
result = (min(A,B,C),max(A,B,C))
print(*result if isinstance(result, tuple) else (result,))
