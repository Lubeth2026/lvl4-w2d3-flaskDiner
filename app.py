
from flask import Flask, request
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

@app.route("/menu", methods=["POST"])
def add_food():
    data = get_menu()

    new_food = request.get_json()

    data.append(new_food)

    save_menu(data)

    return {
        "message": "Food was added successfully", "food": new_food
    }, 201
