"""Proc47. Используя функцию NOD2 из задания Proc46, описать процедуру Frac1(a, b, p, q), преобразующую дробь a/b к несократимому виду p/q (все параметры процедуры — целого типа, a и b — входные, p и q — выходные). 38 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4 Знак результирующей дроби p/q приписывается числителю (т. е. q > 0). С помощью Frac1 найти несократимые дроби, равные a/b + c/d, a/b + e/f, a/b + g/h (числа a, b, c, d, e, f, g, h даны)."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    from fractions import Fraction; a,b,c,d,e,f,g,h=map(int,v); return [str(Fraction(a,b)+Fraction(x,y)) for x,y in ((c,d),(e,f),(g,h))]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
