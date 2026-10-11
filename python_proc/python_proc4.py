"""Proc4*. Описать процедуру TrianglePS(a, P, S), вычисляющую по стороне a равностороннего треугольника его периметр P = 3·a и площадь S = a2· √ 3/4 (a — входной, P и S — выходные параметры; все параметры являются ве- щественными). С помощью этой процедуры найти периметры и площади трех равносторонних треугольников с данными сторонами."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [(3*x,x*x*3**0.5/4) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
