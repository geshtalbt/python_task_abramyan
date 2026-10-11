"""Proc14. Описать процедуру ShiftRight3(A, B, C), выполняющую правый цик- лический сдвиг: значение A переходит в B, значение B — в C, значение C — в A (A, B, C — вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой процедуры выполнить правый циклический сдвиг для двух данных наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2)."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [(v[i+2],v[i],v[i+1]) for i in (0,3)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
