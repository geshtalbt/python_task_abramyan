price = float(input("Enter price for candies: "))
for i in range(12, 21, 2):
    weight = i / 10
    cost = price * weight
    print(f"{weight} кг -> {cost}")