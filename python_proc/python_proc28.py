"""Proc28. Описать функцию IsPrime(N) логического типа, возвращающую TRUE, если целый параметр N (> 1) является простым числом, и FALSE в против- ном случае (число, большее 1, называется простым, если оно не имеет положительных делителей, кроме 1 и самого себя). Дан набор из 10 це- лых чисел, больших 1. С помощью функции IsPrime найти количество простых чисел в данном наборе."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return sum(int(x)>1 and all(int(x)%d for d in range(2,int(int(x)**.5)+1)) for x in v)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
