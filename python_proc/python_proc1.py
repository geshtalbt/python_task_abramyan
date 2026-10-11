"""Proc1. Описать процедуру PowerA3(A, B), вычисляющую третью степень чис- ла A и возвращающую ее в переменной B (A — входной, B — выходной параметр; оба параметра являются вещественными). С помощью этой процедуры найти третьи степени пяти данных чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [x**3 for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
