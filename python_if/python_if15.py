"""If15. Даны три числа. Найти сумму двух наибольших из них."""
import math
A, B, C = map(float, input().split())
result = sum(sorted((A,B,C))[1:])
print(*result if isinstance(result, tuple) else (result,))
