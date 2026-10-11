"""If26*. Для данного вещественного x найти значение следующей функции f, принимающей вещественные значения: −x, если x ≤0, f (x) = x2, если 0 < x < 2, 4, если x ≥2."""
import math
x, = map(float, input().split())
result = -x if x<=0 else x*x if x<2 else 4
print(*result if isinstance(result, tuple) else (result,))
