"""Proc3. Описать процедуру Mean(X, Y, AMean, GMean), вычисляющую среднее арифметическое AMean = (X+Y)/2 и среднее геометрическое Процедуры и функции 31 GMean = √ X·Y двух положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные параметры вещественного типа). С помощью этой процедуры найти среднее арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    a,b,c,d=v; return [((a+x)/2,(a*x)**0.5) for x in (b,c,d)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
