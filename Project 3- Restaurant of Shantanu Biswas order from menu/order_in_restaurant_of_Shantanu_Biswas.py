#will be working in dictionary data type
#Define the menu of restaurant
menu = {
    'Pizza': 50,
    'Pasta': 40,
    'Dhosha': 45,
    'Idli': 35,
    'Burger': 30,
    'Coffee': 10,
    'Tea': 5,
}

print(menu)

#greet the customer
print("Welcome to the restaurant of Shantanu Biswas !!")
print("Pizza: Rs.40\nPasta: Rs.40\nDhosha: Rs. 45\nIdli: Rs.35\nBurger: Rs.30\nCoffee: Rs.10\nTea: Rs.5")

order_total = 0
#80 + 70 = 150

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]     #0 + 40 = 40
    print(f"Your item has been added to the order")
else:
    print(f"Please order something else from the menu. Since your ordered item {item_1} is not available  in out menu")

another_order = input("Do you want to add another item? (YES/NO)")
if another_order == "YES":
    item_2 = input("Enter the name of second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your second order {item_2} is added to the order list ")
    else:
        print(f"Ordered item {item_2} is not available.")

print(f"The total amount of the order is = {order_total}")
