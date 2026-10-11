"""Proc54. Используя функцию MonthDays из задания Proc53, описать процедуру PrevDate(D, M, Y), которая по информации о правильной дате, включа- ющей день D, номер месяца M и год Y, определяет предыдущую дату (параметры целого типа D, M, Y являются одновременно входными и выходными). Применить процедуру PrevDate к трем исходным датам и вывести полученные значения предыдущих дат."""
import math
from math import sqrt
def solve(*values):
    v=list(values)
    import datetime; return [(datetime.date(y,m,d)-datetime.timedelta(days=1)).isoformat() for d,m,y in zip(map(int,v[::3]),map(int,v[1::3]),map(int,v[2::3]))]
if __name__ == "__main__":
    data=list(map(float,input().split()))
    print(solve(*data))
