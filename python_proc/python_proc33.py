"""Proc33. Описать функцию RadToDeg(R) вещественного типа, находящую ве- личину угла в градусах, если дана его величина R в радианах (R — веще- ственное число, 0 < R < 2·π). Воспользоваться следующим соотношением: 180◦= π радианов. В качестве значения π использовать 3.14. С помощью функции RadToDeg перевести из радианов в градусы пять данных углов."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [x*180/3.14 for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
