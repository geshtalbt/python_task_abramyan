"""Boolean25. Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит во второй координатной четверти»."""
x, y = map(int, input().split())
condition = x<0 and y>0
print("TRUE" if condition else "FALSE")
