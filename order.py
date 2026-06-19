
from manager import get_menu, save_menu

# print("Greetings!")

data = get_menu()

food = input("Enter the food item name: ")
description = input("Brief description of food: ")
price = input("How much: ")
category = input("What type of food item is it: ")

new_food = {
    "food": food, "description": description, "price": price, "category": category
}
data.append(new_food)
save_menu(data)
print(f"{new_food} was added to the Menu!")
