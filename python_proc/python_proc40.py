"""Proc40. Описать функцию Exp1(x, ε) вещественного типа (параметры x, ε — вещественные, ε > 0), находящую приближенное значение функции exp(x): exp(x) = 1 + x + x2/(2!) + x3/(3!) + . . . + xn/(n!) + . . . (n! = 1·2·. . .·n). В сумме учитывать все слагаемые, большие ε. С помощью Exp1 найти приближенное значение экспоненты для данного x при шести данных ε."""
import math
from math import sqrt
def solve(*values):
    v = list(values)
    x, eps = v
    total = term = 1.0
    i = 1
    while abs(term) > eps:
        term *= x / i
        total += term
        i += 1
    return total
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
