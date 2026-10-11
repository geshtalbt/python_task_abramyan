"""If12*. Даны три числа. Найти наименьшее из них."""
import math
A, B, C = map(float, input().split())
result = min(A,B,C)
print(*result if isinstance(result, tuple) else (result,))
