"""Boolean5. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A ≥0 или B < −2»."""
A, B = map(int, input().split())
condition = A >= 0 or B < -2
print("TRUE" if condition else "FALSE")
