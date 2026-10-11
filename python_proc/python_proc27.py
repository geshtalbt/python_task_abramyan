"""Proc27. Описать функцию IsPowerN(K, N) логического типа, возвращающую TRUE, если целый параметр K (> 0) является степенью числа N (> 1), и FALSE в противном случае. Дано число N (> 1) и набор из 10 целых по- ложительных чисел. С помощью функции IsPowerN найти количество степеней числа N в данном наборе."""
import math
from math import sqrt
def solve(*values):
    base = int(values[0])
    def is_power(k):
        if k <= 0:
            return False
        while k % base == 0:
            k //= base
        return k == 1
    return sum(is_power(int(x)) for x in values[1:])
if __name__ == "__main__":
    print(solve(*map(int, input().split())))
