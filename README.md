# Flask Virtual Diner API

## Overview
This project is a simple Flask API that manges a virtual diner menu. The API allows users to view the menu, search for food items by name,and add new food items to the menu.

### Routes 
1. GET/
Returns a welcome message
2. GET/menu
Returns all menu items from the menu
3. GET/menu/food/<food_name>
Returns a specific food item based on its name 
4. POST/menu
Adds a new food item to the menu

#### How to run the Server
1. Open a terminal in project folder
2. Activate your virtual environment 
3. Run the Flask App
python app.py
4. The server will start on
http://127.0.0.1:5000

##### How to test a route on Postman
1. Open postman
2. Select the GET method
3. Enter the URL
http://127.0.0.1:5000/menu
4. Click SEND
5. Response should display all menu items stored in the API
