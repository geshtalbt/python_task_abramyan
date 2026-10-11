"""Proc46. Описать функцию NOD2(A, B) целого типа, находящую наибольший общий делитель (НОД) двух целых положительных чисел A и B, используя алгоритм Евклида: НОД(A, B) = НОД(B, A mod B), если B̸ = 0; НОД(A, 0) = A. С помощью этой функции найти наибольшие общие делители пар (A, B), (A, C), (A, D), если даны числа A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; return [math.gcd(int(v[0]),int(x)) for x in v[1:]]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
