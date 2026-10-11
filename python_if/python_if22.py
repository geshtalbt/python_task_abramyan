"""If22*. Даны координаты точки, не лежащей на координатных осях OX и OY. Определить номер координатной четверти, в которой находится данная точка."""
import math
x, y = map(float, input().split())
result = 1 if x>0 and y>0 else 2 if x<0<y else 3 if x<0 and y<0 else 4
print(*result if isinstance(result, tuple) else (result,))
