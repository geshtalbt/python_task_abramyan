"""If11. Даны две переменные целого типа: A и B. Если их значения не равны, то присвоить каждой переменной большее из этих значений, а если равны, то присвоить переменным нулевые значения. Вывести новые значения переменных A и B."""
import math
A, B = map(int, input().split())
result = (max(A,B),max(A,B)) if A!=B else (0,0)
print(*result if isinstance(result, tuple) else (result,))
