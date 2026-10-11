"""Proc21*. Описать функцию SumRange(A, B) целого типа, находящую сумму всех целых чисел от A до B включительно (A и B — целые). Если A > B, то функция возвращает 0. С помощью этой функции найти суммы чисел от A до B и от B до C, если даны числа A, B, C."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    a,b,c=map(int,v); return sum(range(a,b+1)) if a<=b else 0, sum(range(b,c+1)) if b<=c else 0
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
