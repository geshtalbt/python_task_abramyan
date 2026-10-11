"""Boolean23. Дано четырехзначное число. Проверить истинность высказыва- ния: «Данное число читается одинаково слева направо и справа налево»."""
A, = map(int, input().split())
d = [int(c) for c in str(abs(A))]
condition = A==D and B==C
print("TRUE" if condition else "FALSE")
