"""If18. Даны три целых числа, одно из которых отлично от двух других, рав- ных между собой. Определить порядковый номер числа, отличного от остальных."""
import math
A, B, C = map(int, input().split())
result = next(i+1 for i,x in enumerate((A,B,C)) if (A,B,C).count(x)==1)
print(*result if isinstance(result, tuple) else (result,))
