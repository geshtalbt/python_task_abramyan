"""Proc58. Используя функции Leng и Perim из заданий Proc56 и Proc57, описать функцию Area(xA, yA, xB, yB, xC, yC) вещественного типа, находящую площадь треугольника ABC по формуле SABC = √p·(p−|AB|)·(p−|AC|)·(p−|BC|), где p — полупериметр. С помощью этой функции найти площади тре- угольников ABC, ABD, ACD, если даны координаты точек A, B, C, D."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import math; pts=[tuple(v[i:i+2]) for i in range(0,len(v),2)]; A,B,C,D=pts; area=lambda p,q,r: math.sqrt(max(0,(sum(math.dist(u,w) for u,w in ((p,q),(p,r),(q,r)))/2)*__import__("functools").reduce(lambda a,z:a*(sum(math.dist(u,w) for u,w in ((p,q),(p,r),(q,r)))/2-z),[math.dist(p,q),math.dist(p,r),math.dist(q,r)],1))); return [area(A,B,C),area(A,B,D),area(A,C,D)]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
