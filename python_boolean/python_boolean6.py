"""Boolean6. Даны три целых числа: A, B, C. Проверить истинность высказыва- ния: «Справедливо двойное неравенство A < B < C»."""
A, B, C = map(int, input().split())
condition = A < B < C
print("TRUE" if condition else "FALSE")
