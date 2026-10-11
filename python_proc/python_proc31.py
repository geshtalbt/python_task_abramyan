"""Proc31. Описать функцию IsPalindrom(K), возвращающую TRUE, если целый параметр K (> 0) является палиндромом (то есть его запись читается оди- наково слева направо и справа налево), и FALSE в противном случае. С ее помощью найти количество палиндромов в наборе из 10 целых поло- жительных чисел. При описании функции можно использовать функции DigitCount и DigitN из заданий Proc29 и Proc30."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return sum(str(int(x))==str(int(x))[::-1] for x in v)
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
