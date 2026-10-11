"""Proc39. Используя функции Power1 и Power2 (задания Proc37 и Proc38), опи- сать функцию Power3(A, B) вещественного типа с вещественными па- раметрами, находящую AB следующим образом: если B имеет нулевую дробную часть, то вызывается функция Power2(A, Round(B)); в против- ном случае вызывается функция Power1(A, B). С помощью этой функции найти AP, BP, CP, если даны числа P, A, B, C."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    p,a,b,c=v; return [x**p if x>0 or p==int(p) else 0 for x in (a,b,c)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
