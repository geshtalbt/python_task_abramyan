"""Proc38. Описать функцию Power2(A, N) вещественного типа, находящую ве- личину AN (A — вещественный, N — целый параметр) по следующим формулам: A0 = 1; AN = A·A·. . .·A (N сомножителей), если N > 0; AN = 1/(A·A·. . .·A) (|N| сомножителей), если N < 0. С помощью этой функции найти AK, AL, AM, если даны числа A, K, L, M."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    a,k,l,m=v; return [a**int(q) for q in (k,l,m)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
