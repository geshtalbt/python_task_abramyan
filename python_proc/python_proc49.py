"""Proc49. Учитывая соотношение НОД(A, B, C) = НОД(НОД(A, B), C) и исполь- зуя функцию NOD2 из задания Proc46, описать функцию NOD3(A, B, C) целого типа, находящую наибольший общий делитель трех целых поло- жительных чисел A, B, C. С помощью этой функции найти наибольшие общие делители троек (A, B, C), (A, C, D) и (B, C, D), если даны числа A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; a,b,c,d=map(int,v); return [math.gcd(*map(int,x)) for x in ((a,b,c),(a,c,d),(b,c,d))]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
