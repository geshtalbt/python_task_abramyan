"""If9. Даны две переменные вещественного типа: A, B. Перераспределить значе- ния данных переменных так, чтобы в A оказалось меньшее из значений, а в B — большее. Вывести новые значения переменных A и B."""
import math
A, B = map(float, input().split())
result = (min(A,B),max(A,B))
print(*result if isinstance(result, tuple) else (result,))
