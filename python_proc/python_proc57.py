"""Proc57. Используя функцию Leng из задания Proc56, описать функцию Perim(xA, yA, xB, yB, xC, yC) вещественного типа, находящую периметр треугольника ABC по координатам его вершин (xA, yA, xB, yB, xC, yC — вещественные параметры). С помощью этой функции найти периметры треугольников ABC, ABD, ACD, если даны координаты точек A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; pts=[tuple(v[i:i+2]) for i in range(0,len(v),2)]; A,B,C,D=pts; dist=lambda p,q: math.dist(p,q); return [dist(A,B)+dist(A,C)+dist(B,C),dist(A,B)+dist(A,D)+dist(B,D),dist(A,C)+dist(A,D)+dist(C,D)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
