"""Proc6. Описать процедуру DigitCountSum(K, C, S), находящую количество C цифр целого положительного числа K, а также их сумму S (K — входной, C и S — выходные параметры целого типа). С помощью этой процедуры найти количество и сумму цифр для каждого из пяти данных целых чисел."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [(len(str(int(x)),),sum(map(int,str(int(x)))) ) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
