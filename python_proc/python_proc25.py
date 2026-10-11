"""Proc25. Описать функцию IsSquare(K) логического типа, возвращающую TRUE, если целый параметр K (> 0) является квадратом некоторого це- лого числа, и FALSE в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых положительных чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return sum(math.isqrt(int(x))**2==int(x) for x in v)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
