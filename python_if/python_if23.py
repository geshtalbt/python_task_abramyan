"""If23. Даны целочисленные координаты трех вершин прямоугольника, стороны которого параллельны координатным осям. Найти координаты его четвер- той вершины."""
import math
x1, y1, x2, y2, x3, y3 = map(int, input().split())
result = (x1 if x1==x2 else x3,y1 if y1==y2 else y3)
print(*result if isinstance(result, tuple) else (result,))
