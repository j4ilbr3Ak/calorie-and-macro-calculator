Calorie & Macro Calculator

This is a terminal-based calorie and macronutrient calculator. The program allows users to enter their personal information, track multiple foods, and calculate their daily calorie needs and macronutrients (calories, protein, carbs, fat). The program stores food data in a local database and fetches missing food information from the Open Food Facts API.
Features

    Calculate Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation (Imperial units).
    Calculate daily calorie needs based on activity level.
    Track multiple food items and calculate total macros (calories, protein, carbs, fat).
    Automatically store food information in a local SQLite database.
    Fetch missing food data from the Open Food Facts API and save it for future use.

Requirements

To run the program, you will need:

    Python 3.x
    requests library for API requests
    SQLite (bundled with Python)

Install the required Python libraries by running:

pip install requests

Setup Instructions

Initialize the Database: Before running the main program, initialize the SQLite database by running the database.py script. This will create the necessary table to store food data.

python database.py

Run the Main Program: After the database is initialized, you can run the main program calorie_calculator.py:

    python calorie_calculator.py

    Interact with the Program: The program will prompt you for your personal details (name, age, gender, weight, height, and activity level) and a list of foods you consumed. You can enter multiple food items separated by commas.

    Food Data Storage: If the food is not already in the local database, the program will fetch the information from the Open Food Facts API and store it in the database for future use.

File Descriptions

    database.py: Handles database operations (creating the table, saving food data, fetching food data from the local database).
    api_intergration.py: Handles interactions with the Open Food Facts API to fetch food data when it's not found in the local database.
    calorie_calculator.py: Main program that handles user input, calculates BMR and daily calories, tracks multiple foods, and calculates macros.

Example Usage

Here is a sample interaction with the program:

Welcome to the Calorie & Macro Calculator!
Enter your name: John
Enter your age: 30
Enter your gender (male/female): male
Enter your weight in LBS: 180
Enter your height in IN: 70
Activity levels: sedentary, lightly active, moderately active, very active
Enter your activity level: moderately active
Enter the food items you ate (separate by commas): apple, chicken breast

The program will calculate your BMR, daily calorie needs, and track the macros for the foods you entered. If a food is not in the database, it will be fetched from the Open Food Facts API and saved for future use.
Troubleshooting

    If the program is not fetching food data from the API, check your internet connection.
    Make sure you have correctly initialized the database by running food_database.py.
    Ensure that the food items are entered correctly (e.g., avoid extra spaces).
