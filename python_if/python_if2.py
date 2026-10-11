"""If2. Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае вычесть из него 2. Вывести полученное число."""
import math
A, = map(int, input().split())
result = A+1 if A>0 else A-2
print(*result if isinstance(result, tuple) else (result,))
