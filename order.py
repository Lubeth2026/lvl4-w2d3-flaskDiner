
import json

# print("Greetings!")

ORDERS_FILE = "menu.json"

# Function for loading the menu items READ
def menu_items():
    with open(ORDERS_FILE, "r") as file:
        return json.load(file)
    
print(menu_items())