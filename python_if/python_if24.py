"""If24. Для данного вещественного x найти значение следующей функции f, принимающей вещественные значения: f (x) = 2·sin(x), если x > 0, 6 −x, если x ≤0."""
import math
x, = map(float, input().split())
result = 2*math.sin(x) if x>0 else 6-x
print(*result if isinstance(result, tuple) else (result,))
