"""If27. Для данного вещественного x найти значение следующей функции f, принимающей значения целого типа: 0, если x < 0, f (x) = 1, если x принадлежит [0, 1), [2, 3), . . . , −1, если x принадлежит [1, 2), [3, 4), . . . ."""
import math
x, = map(float, input().split())
result = 0 if x<0 else 1 if int(x)%2==0 else -1
print(*result if isinstance(result, tuple) else (result,))
