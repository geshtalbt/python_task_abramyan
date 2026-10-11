"""Proc45. Описать функцию Power4(x, a, ε) вещественного типа (параметры x, a, ε — вещественные, |x| < 1; a, ε > 0), находящую приближенное значение функции (1 + x)a: (1 + x)a = 1 + a·x + a·(a−1)·x2/(2!) + . . . + a·(a−1)·. . .·(a−n+1)·xn/(n!) + . . . . В сумме учитывать все слагаемые, модуль которых больше ε. С помощью Power4 найти приближенное значение (1 + x)a для данных x и a при шести данных ε."""
import math
from math import sqrt
def solve(*values):
    v = list(values)
    x, a, eps = v
    total = 1.0
    term = 1.0
    coeff = a
    i = 1
    while abs(term) > eps:
        term = coeff * x**i
        total += term
        coeff *= (a-i)/(i+1)
        i += 1
    return total
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
