"""Proc42. Описать функцию Cos1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0), находящую приближенное значение функции cos(x): cos(x) = 1 −x2/(2!) + x4/(4!) −. . . + (−1)n·x2·n/((2·n)!) + . . . . В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Cos1 найти приближенное значение косинуса для данного x при шести данных ε."""
import math
from math import sqrt
def solve(*values):
    v = list(values)
    x, eps = v
    total = term = 1.0
    i = 1
    while abs(term) > eps:
        term *= -x*x / ((2*i-1)*(2*i))
        total += term
        i += 1
    return total
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
