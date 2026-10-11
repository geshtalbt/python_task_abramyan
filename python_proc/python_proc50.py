"""Proc50. Описать процедуру TimeToHMS(T, H, M, S), определяющую по вре- мени T (в секундах) содержащееся в нем количество часов H, минут M и секунд S (T — входной, H, M и S — выходные параметры целого типа). Используя эту процедуру, найти количество часов, минут и секунд для пяти данных отрезков времени T1, T2, . . ., T5."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [(int(x)//3600,(int(x)%3600)//60,int(x)%60) for x in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
