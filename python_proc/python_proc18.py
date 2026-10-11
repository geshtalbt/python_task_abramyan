"""Proc18. Описать функцию CircleS(R) вещественного типа, находящую пло- щадь круга радиуса R (R — вещественное). С помощью этой функции найти площади трех кругов с данными радиусами. Площадь круга ради- уса R вычисляется по формуле S = π·R2. В качестве значения π использо- вать 3.14."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [3.14*x*x for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
