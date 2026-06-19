
from flask import Flask
from manager import get_menu, save_menu

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Welcome to the Flask Virtual Diner!"
    }

@app.route("/menu")
def menu():
    return (get_menu())

@app.route("/menu/food/<food_name>")
def get_item_by_name(food_name):
    data = get_menu()

    for item in data:
        if item["food"].lower() == food_name.lower():
            return item
        
    return {"message": "Food item not found."}
