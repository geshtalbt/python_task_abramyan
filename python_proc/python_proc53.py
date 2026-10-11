"""Proc53. Используя функцию IsLeapYear из задания Proc52, описать функцию MonthDays(M, Y) целого типа, которая возвращает количество дней для M-го месяца года Y (1 ≤M ≤12, Y > 0 — целые числа). Вывести значение функции MonthDays для данного года Y и месяцев M1, M2, M3. Процедуры и функции 39"""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    y=int(v[0]); return [29 if int(m)==2 and (y%400==0 or y%4==0 and y%100!=0) else [31,28,31,30,31,30,31,31,30,31,30,31][int(m)-1] for m in v[1:]]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
