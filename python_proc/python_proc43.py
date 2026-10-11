"""Proc43. Описать функцию Ln1(x, ε) вещественного типа (параметры x, ε — вещественные, |x| < 1, ε > 0), находящую приближенное значение функции ln(1 + x): ln(1 + x) = x −x2/2 + x3/3 −. . . + (−1)n·xn+1/(n+1) + . . . . В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Ln1 найти приближенное значение ln(1 + x) для данного x при шести данных ε."""
import math
from math import sqrt
def solve(*values):
    v = list(values)
    x, eps = v
    total = term = x
    i = 2
    while abs(term) > eps:
        term *= -x*(i-1)/i
        total += term
        i += 1
    return total
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
