"""Proc29. Описать функцию DigitCount(K) целого типа, находящую количество цифр целого положительного числа K. Используя эту функцию, найти ко- личество цифр для каждого из пяти данных целых положительных чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [len(str(int(x))) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
