"""Boolean22. Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую или убывающую после- довательность»."""
A, = map(int, input().split())
d = [int(c) for c in str(abs(A))]
condition = d[0]<d[1]<d[2] or d[0]>d[1]>d[2]
print("TRUE" if condition else "FALSE")
