"""If6*. Даны два числа. Вывести большее из них."""
import math
A, B = map(float, input().split())
result = max(A,B)
print(*result if isinstance(result, tuple) else (result,))
