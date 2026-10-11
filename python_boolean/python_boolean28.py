"""Boolean28. Даны числа x, y. Проверить истинность высказывания: «Точка с координатами (x, y) лежит в первой или третьей координатной четверти»."""
x, y = map(int, input().split())
condition = x>0 and y>0 or x<0 and y<0
print("TRUE" if condition else "FALSE")
