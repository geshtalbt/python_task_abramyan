"""If8*. Даны два числа. Вывести вначале большее, а затем меньшее из них."""
import math
A, B = map(float, input().split())
result = (max(A,B),min(A,B))
print(*result if isinstance(result, tuple) else (result,))
