"""Proc59. Используя функции Leng и Area из заданий Proc56 и Proc58, описать функцию Dist(xP, yP, xA, yA, xB, yB) вещественного типа, находящую расстояние D(P, AB) от точки P до прямой AB по формуле D(P, AB) = 2·SPAB/|AB|, где SPAB — площадь треугольника PAB. С помощью этой функции найти расстояния от точки P до прямых AB, AC, BC, если даны координаты точек P, A, B, C."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; P,A,B,C=[tuple(v[i:i+2]) for i in range(0,8,2)]; dist=lambda p,a,b: abs((b[0]-a[0])*(a[1]-p[1])-(a[0]-p[0])*(b[1]-a[1]))/math.dist(a,b); return [dist(P,A,B),dist(P,A,C),dist(P,B,C)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
