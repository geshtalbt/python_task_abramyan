price = float(input('Enter price for candies: '))
for i in range(1 , 10):
    print(f'Price for 0.{i} kg candies: {price * i/10}')
    print(f'Price for 1kg candies: {price * 10/10}')
    