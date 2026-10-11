"""Proc9. Описать процедуру AddLeftDigit(D, K), добавляющую к целому по- ложительному числу K слева цифру D (D — входной параметр целого типа, лежащий в диапазоне 1–9, K — параметр целого типа, являющийся одновременно входным и выходным). С помощью этой процедуры после- довательно добавить к данному числу K слева данные цифры D1 и D2, выводя результат каждого добавления. 32 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4"""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    k,d1,d2=map(int,v); k=int(str(d1)+str(k)); return (k,int(str(d2)+str(k)))
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
