"""Proc30. Описать функцию DigitN(K, N) целого типа, возвращающую N-ю циф- ру целого положительного числа K (цифры в числе нумеруются справа Процедуры и функции 35 налево). Если количество цифр в числе K меньше N, то функция возвра- щает −1. Для каждого из пяти данных целых положительных чисел K1, K2, . . ., K5 вызвать функцию DigitN с параметром N, изменяющимся от 1 до 5."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [[(int(x)//10**(n-1))%10 if len(str(int(x)))>=n else -1 for n in range(1,6)] for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
