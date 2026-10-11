"""If3. Дано целое число. Если оно является положительным, то прибавить к нему 1; если отрицательным, то вычесть из него 2; если нулевым, то заменить его на 10. Вывести полученное число."""
import math
A, = map(int, input().split())
result = A+1 if A>0 else A-2 if A<0 else 10
print(*result if isinstance(result, tuple) else (result,))
