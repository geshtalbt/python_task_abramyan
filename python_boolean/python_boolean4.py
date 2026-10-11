"""Boolean4. Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤3»."""
A, B = map(int, input().split())
condition = A > 2 and B <= 3
print("TRUE" if condition else "FALSE")
