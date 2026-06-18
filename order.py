
import json

# print("Greetings!")

ORDERS_FILE = "menu.json"

# Function for loading the menu items READ
def menu_items():
    with open(ORDERS_FILE, "r") as file:
        return json.load(file)

# Function that accepts data & WRITES it in the menu.json file
def save_items(data):
    with open(ORDERS_FILE, "w") as file:
        json.dump(data, file, indent=5)

data = menu_items()

food = input("Enter the food item name: ")
description = input("Brief description of food: ")
price = input("How much: ")
category = input("What type of food item is it: ")

new_food = {
    "food": food, "description": description, "price": price, "category": category
}
data.append(new_food)
save_items(data)
print(f"{new_food} was added to the Menu!")

print(menu_items())