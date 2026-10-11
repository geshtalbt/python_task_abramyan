"""Proc11. Описать процедуру Minmax(X, Y), записывающую в переменную X минимальное из значений X и Y, а в переменную Y — максимальное из этих значений (X и Y — вещественные параметры, являющиеся одновре- менно входными и выходными). Используя четыре вызова этой процеду- ры, найти минимальное и максимальное из данных чисел A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return min(v),max(v)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
