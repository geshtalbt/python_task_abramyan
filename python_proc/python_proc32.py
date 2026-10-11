"""Proc32. Описать функцию DegToRad(D) вещественного типа, находящую ве- личину угла в радианах, если дана его величина D в градусах (D — веще- ственное число, 0 < D < 360). Воспользоваться следующим соотношением: 180◦= π радианов. В качестве значения π использовать 3.14. С помощью функции DegToRad перевести из градусов в радианы пять данных углов."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [x*3.14/180 for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
