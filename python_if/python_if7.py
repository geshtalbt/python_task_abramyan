"""If7. Даны два числа. Вывести порядковый номер меньшего из них."""
import math
A, B = map(float, input().split())
result = 1 if A<B else 2
print(*result if isinstance(result, tuple) else (result,))
