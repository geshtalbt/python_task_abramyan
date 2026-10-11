"""Proc48. Учитывая, что наименьшее общее кратное двух целых положитель- ных чисел A и B равно A·(B/НОД(A, B)), где НОД(A, B) — наибольший общий делитель A и B, и используя функцию NOD2 из задания Proc46, описать функцию NOK2(A, B) целого типа, находящую наименьшее об- щее кратное чисел A и B. С помощью NOK2 найти наименьшие общие кратные пар (A, B), (A, C), (A, D), если даны числа A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; a,b,c,d=map(int,v); return [math.lcm(a,x) for x in (b,c,d)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
