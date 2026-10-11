"""Boolean19. Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных»."""
A, B, C = map(int, input().split())
condition = A==-B or A==-C or B==-C
print("TRUE" if condition else "FALSE")
