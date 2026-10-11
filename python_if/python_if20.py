"""If20. На числовой оси расположены три точки: A, B, C. Определить, какая из двух последних точек (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A."""
import math
A, B, C = map(float, input().split())
result = (B,abs(B-A)) if abs(B-A)<abs(C-A) else (C,abs(C-A))
print(*result if isinstance(result, tuple) else (result,))
