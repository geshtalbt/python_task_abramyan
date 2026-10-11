"""If4*. Даны три целых числа. Найти количество положительных чисел в исход- ном наборе."""
import math
A, B, C = map(int, input().split())
result = sum(x>0 for x in (A,B,C))
print(*result if isinstance(result, tuple) else (result,))
