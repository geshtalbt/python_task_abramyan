"""Proc26. Описать функцию IsPower5(K) логического типа, возвращающую TRUE, если целый параметр K (> 0) является степенью числа 5, и FALSE в противном случае. С ее помощью найти количество степеней числа 5 в наборе из 10 целых положительных чисел."""
import math
from math import sqrt
def solve(*values):
    def is_power5(k):
        if k <= 0:
            return False
        while k % 5 == 0:
            k //= 5
        return k == 1
    return sum(is_power5(int(x)) for x in values)
if __name__ == "__main__":
    print(solve(*map(int, input().split())))
