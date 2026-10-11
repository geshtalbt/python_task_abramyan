"""Proc52. Описать функцию IsLeapYear(Y) логического типа, которая возвраща- ет TRUE, если год Y (целое положительное число) является високосным, и FALSE в противном случае. Вывести значение функции IsLeapYear для пяти данных значений параметра Y. Високосным считается год, делящий- ся на 4, за исключением тех годов, которые делятся на 100 и не делятся на 400."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    return [int(y)%400==0 or (int(y)%4==0 and int(y)%100!=0) for y in v]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
