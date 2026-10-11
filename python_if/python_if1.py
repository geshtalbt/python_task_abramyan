"""If1. Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его. Вывести полученное число."""
import math
A, = map(int, input().split())
result = A+1 if A>0 else A
print(*result if isinstance(result, tuple) else (result,))
