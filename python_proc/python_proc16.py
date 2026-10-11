"""Proc16. Описать функцию Sign(X) целого типа, возвращающую для веще- ственного числа X следующие значения: −1, если X < 0; 0, если X = 0; 1, если X > 0. С помощью этой функции найти значение выражения Sign(A) + Sign(B) для данных вещественных чисел A и B."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return (1 if v[0]>0 else -1 if v[0]<0 else 0)+(1 if v[1]>0 else -1 if v[1]<0 else 0)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
