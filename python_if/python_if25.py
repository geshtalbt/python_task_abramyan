"""If25. Для данного целого x найти значение следующей функции f, принимаю- щей значения целого типа: 16 М. Э. Абрамян. Электронный задачник Programming Taskbook 4.4 f (x) = 2·x, если x < −2 или x > 2, −3·x, в противном случае."""
import math
x, = map(int, input().split())
result = 2*x if x < -2 or x > 2 else -3*x
print(*result if isinstance(result, tuple) else (result,))
