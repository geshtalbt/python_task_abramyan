"""Proc36. Описать функцию Fib(N) целого типа, вычисляющую N-й элемент последовательности чисел Фибоначчи FK, которая описывается следую- щими формулами: 36 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4 F1 = 1, F2 = 1, FK = FK−2 + FK−1, K = 3, 4, . . . . Используя функцию Fib, найти пять чисел Фибоначчи с данными номе- рами N1, N2, . . ., N5. Дополнительные задания на процедуры и функции"""
import math
from math import sqrt
def solve(*values):
    def fib(n):
        a = b = 1
        if n <= 2:
            return 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b
    return [fib(int(x)) for x in values]
if __name__ == "__main__":
    data = list(map(float, input().split()))
    print(solve(*data))
