"""Case8. Даны два целых числа: D (день) и M (месяц), определяющие пра- вильную дату невисокосного года. Вывести значения D и M для даты, предшествующей указанной."""
import calendar
d,m=map(int,input().split());
if d>1:d-=1
elif m>1:m-=1;d=calendar.monthrange(2021,m)[1]
else:d,m=31,12
print(d,m)
