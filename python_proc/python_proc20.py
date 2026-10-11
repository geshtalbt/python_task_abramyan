"""Proc20. Описать функцию TriangleP(a, h), находящую периметр равнобед- ренного треугольника по его основанию a и высоте h, проведенной к основанию (a и h — вещественные). С помощью этой функции найти периметры трех треугольников, для которых даны основания и высоты. Для нахождения боковой стороны b треугольника использовать теорему Пифагора: b2 = (a/2)2 + h2."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return [a+2*math.sqrt((a/2)**2+h*h) for a,h in zip(v[::2],v[1::2])]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
