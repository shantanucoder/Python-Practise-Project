# Define the menu of the restaurant
menu = {
    'Pizza': 50,
    'Pasta': 40,
    'Dhosha': 45,
    'Idli': 35,
    'Burger': 30,
    'Coffee': 10,
    'Tea': 5,
}

# Display the menu
print("Welcome to the restaurant of Shantanu Biswas !!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

order_total = 0  # Initialize total order cost

# Take the first order
item_1 = input("Enter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to the order.")
else:
    print(f"Sorry, the item '{item_1}' is not available in our menu.")

# Ask if the customer wants to order another item
another_order = input("Do you want to add another item? (YES/NO): ").strip().lower()
if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").strip().title()
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to the order.")
    else:
        print(f"Sorry, the item '{item_2}' is not available in our menu.")
elif another_order != "no":
    print("Invalid response. Please type 'YES' or 'NO'.")

# Display the total order cost
print(f"The total amount for your order is: Rs.{order_total}")
