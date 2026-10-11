"""Proc51. Описать процедуру IncTime(H, M, S, T), которая увеличивает на T се- кунд время, заданное в часах H, минутах M и секундах S (H, M и S — входные и выходные параметры, T — входной параметр; все параметры — целые положительные). Дано время (в часах H, минутах M, секундах S) и целое число T. Используя процедуру IncTime, увеличить данное время на T секунд и вывести новые значения H, M, S."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    h,m,s,t=map(int,v); q=h*3600+m*60+s+t; return q//3600,(q%3600)//60,q%60
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
