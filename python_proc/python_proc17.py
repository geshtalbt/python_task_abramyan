"""Proc17. Описать функцию RootsCount(A, B, C) целого типа, определяющую количество корней квадратного уравнения A·x2 + B·x + C = 0 (A, B, C — вещественные параметры, A̸ = 0). С ее помощью найти количество корней для каждого из трех квадратных уравнений с данными коэффициентами. Количество корней определять по значению дискриминанта: D = B2 −4·A·C."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [2 if b*b-4*a*c>0 else 1 if b*b-4*a*c==0 else 0 for a,b,c in zip(v[::3],v[1::3],v[2::3])]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
