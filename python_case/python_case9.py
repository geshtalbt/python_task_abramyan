"""Case9*. Даны два целых числа: D (день) и M (месяц), определяющие пра- вильную дату невисокосного года. Вывести значения D и M для даты, следующей за указанной."""
import calendar
d,m=map(int,input().split());
if d<calendar.monthrange(2021,m)[1]:d+=1
elif m<12:d,m=1,m+1
else:d,m=1,1
print(d,m)
