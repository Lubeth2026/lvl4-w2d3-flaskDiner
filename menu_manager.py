
import json

ORDERS_FILE = "menu.json"

# Function for loading the menu items READ
def get_menu():
    with open(ORDERS_FILE, "r") as file:
        return json.load(file)

# Function that accepts data & WRITES it in the menu.json file
def save_menu(data):
    with open(ORDERS_FILE, "w") as file:
        json.dump(data, file, indent=5)

