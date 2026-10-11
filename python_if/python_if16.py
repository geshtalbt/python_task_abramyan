"""If16. Даны три переменные вещественного типа: A, B, C. Если их значения упорядочены по возрастанию, то удвоить их; в противном случае заме- нить значение каждой переменной на противоположное. Вывести новые значения переменных A, B, C."""
import math
A, B, C = map(float, input().split())
result = (2*A,2*B,2*C) if A<=B<=C else (-A,-B,-C)
print(*result if isinstance(result, tuple) else (result,))
