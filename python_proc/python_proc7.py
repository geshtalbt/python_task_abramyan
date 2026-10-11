"""Proc7. Описать процедуру InvertDigits(K), меняющую порядок следования цифр целого положительного числа K на обратный (K — параметр целого типа, являющийся одновременно входным и выходным). С помощью этой процедуры поменять порядок следования цифр на обратный для каждого из пяти данных целых чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [int(str(int(x))[::-1]) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
