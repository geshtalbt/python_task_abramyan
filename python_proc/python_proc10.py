"""Proc10. Описать процедуру Swap(X, Y), меняющую содержимое перемен- ных X и Y (X и Y — вещественные параметры, являющиеся одновременно входными и выходными). С ее помощью для данных переменных A, B, C, D последовательно поменять содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    a,b,c,d=v; a,b=b,a; c,d=d,c; b,c=c,b; return a,b,c,d
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
