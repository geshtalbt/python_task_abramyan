"""Proc13. Описать процедуру SortDec3(A, B, C), меняющую содержимое пере- менных A, B, C таким образом, чтобы их значения оказались упорядо- ченными по убыванию (A, B, C — вещественные параметры, являющиеся одновременно входными и выходными). С помощью этой процедуры упо- рядочить по убыванию два данных набора из трех чисел: (A1, B1, C1) и (A2, B2, C2)."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [tuple(sorted(v[i:i+3],reverse=True)) for i in (0,3)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
