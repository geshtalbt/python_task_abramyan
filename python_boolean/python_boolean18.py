"""Boolean18. Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара совпадающих»."""
A, B, C = map(int, input().split())
condition = A==B or A==C or B==C
print("TRUE" if condition else "FALSE")
