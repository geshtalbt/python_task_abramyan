"""Proc23. Описать функцию Quarter(x, y) целого типа, определяющую номер координатной четверти, в которой находится точка с ненулевыми веще- ственными координатами (x, y). С помощью этой функции найти номера координатных четвертей для трех точек с данными ненулевыми коорди- натами."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [1 if x>0 and y>0 else 2 if x<0<y else 3 if x<0 and y<0 else 4 for x,y in zip(v[::2],v[1::2])]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
