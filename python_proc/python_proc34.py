"""Proc34. Описать функцию Fact(N) вещественного типа, вычисляющую зна- чение факториала N! = 1·2·. . .·N (N > 0 — параметр целого типа; веще- ственное возвращаемое значение используется для того, чтобы избежать целочисленного переполнения при больших значениях N). С помощью этой функции найти факториалы пяти данных целых чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return [math.factorial(int(x)) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
