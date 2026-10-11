"""Proc37. Описать функцию Power1(A, B) вещественного типа, находящую вели- чину AB по формуле AB = exp(B·ln(A)) (параметры A и B — вещественные). В случае нулевого или отрицательного параметра A функция возвраща- ет 0. С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    p,a,b,c=v; return [x**p if x>0 else 0 for x in (a,b,c)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
