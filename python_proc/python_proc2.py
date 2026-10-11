"""Proc2. Описать процедуру PowerA234(A, B, C, D), вычисляющую вторую, третью и четвертую степень числа A и возвращающую эти степени со- ответственно в переменных B, C и D (A — входной, B, C, D — выходные параметры; все параметры являются вещественными). С помощью этой процедуры найти вторую, третью и четвертую степень пяти данных чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [(x*x,x**3,x**4) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
