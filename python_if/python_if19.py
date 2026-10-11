"""If19. Даны четыре целых числа, одно из которых отлично от трех других, равных между собой. Определить порядковый номер числа, отличного от остальных."""
import math
A, B, C, D = map(int, input().split())
result = next(i+1 for i,x in enumerate((A,B,C,D)) if (A,B,C,D).count(x)==1)
print(*result if isinstance(result, tuple) else (result,))
