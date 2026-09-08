# Shopping Cart Program

foods = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
prices = [1.29, 0.99, 2.49, 3.99, 4.99]
total = 0

while True:
    food = input("Enter the food item you want to add to your cart (or type 'done' to finish): ")
    if food.lower() == "done":
        break
    else:
        price = float(input(f"Enter the price of the {food}: $"))
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price

print()
print(f'your total is: ${total:.2f}')