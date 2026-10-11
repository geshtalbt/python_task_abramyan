"""Proc56. Описать функцию Leng(xA, yA, xB, yB) вещественного типа, находя- щую длину отрезка AB на плоскости по координатам его концов: |AB| = q (xA −xB)2 + (yA −yB)2 (xA, yA, xB, yB — вещественные параметры). С помощью этой функции найти длины отрезков AB, AC, AD, если даны координаты точек A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return [math.hypot(v[0]-x,v[1]-y) for x,y in zip(v[2::2],v[3::2])]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
