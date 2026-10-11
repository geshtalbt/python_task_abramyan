"""Proc24. Описать функцию Even(K) логического типа, возвращающую TRUE, если целый параметр K является четным, и FALSE в противном случае. С ее помощью найти количество четных чисел в наборе из 10 целых чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return sum(int(x)%2==0 for x in v)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
