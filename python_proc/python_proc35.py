"""Proc35. Описать функцию Fact2(N) вещественного типа, вычисляющую двой- ной факториал: N!! = 1·3·5·. . .·N, если N — нечетное; N!! = 2·4·6·. . .·N, если N — четное (N > 0 — параметр целого типа; вещественное возвращаемое значение ис- пользуется для того, чтобы избежать целочисленного переполнения при больших значениях N). С помощью этой функции найти двойные факто- риалы пяти данных целых чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return [math.prod(range(int(x)%2 or 2,int(x)+1,2)) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
