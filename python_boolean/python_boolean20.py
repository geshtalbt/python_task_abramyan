"""Boolean20*. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного числа различны»."""
A, = map(int, input().split())
d = [int(c) for c in str(abs(A))]
condition = len(set(d))==3
print("TRUE" if condition else "FALSE")
