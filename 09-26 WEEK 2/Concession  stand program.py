# Concession stand program

menu = {
    "hot dog": 2.50,
    "popcorn": 3.00,
    "soda": 1.50,
    "nachos": 4.00,
    "fries": 2.00,
    "iced tea": 1.75,
    "lemonade": 1.75
}

cart = []
total = 0.0

print("Welcome to the Concession Stand!")
print("-----Menu-----")
for item, price in menu.items():
    print(f"{item:10}: ${price:.2f}")
print("----------------")

while True:
    item = input("What would you like to order? (or enter 'done' to finish): ").lower()
    if item == "done":
        break
    elif item in menu:
        cart.append(item)
        total += menu[item]
        print(f"{item.title()} added to your cart.")
    else:
        print("Sorry, we don't have that item.")

print("----Your Order Summary----")
for item in cart:
    print(f"- {item.title():10}: ${menu[item]:.2f}")
print(f"Your total is: ${total:.2f}")
print("Please proceed to the payment counter.")
print("------------------------------")