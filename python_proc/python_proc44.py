"""Proc44. Описать функцию Arctg1(x, ε) вещественного типа (параметры x, ε — вещественные, |x| < 1, ε > 0), находящую приближенное значение функции arctg(x): arctg(x) = x −x3/3 + x5/5 −. . . + (−1)n·x2·n+1/(2·n+1) + . . . . В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Arctg1 найти приближенное значение arctg(x) для данного x при шести данных ε."""
import math
from math import sqrt
def solve(*values):
    v = list(values)
    x, eps = v
    total = term = x
    i = 1
    while abs(term) > eps:
        term *= -x*x*(2*i-1)/(2*i+1)
        total += term
        i += 1
    return total
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
