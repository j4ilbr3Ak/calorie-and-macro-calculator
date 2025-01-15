import sqlite3
from api_integration import fetch_and_store_food_data


def search_food_in_database(food_name):
    """
    Search for a food item in the local database.
    """
    conn = sqlite3.connect("food_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM food_items WHERE name LIKE ?", (f"%{food_name}%",))
    results = cursor.fetchall()
    conn.close()
    return results


def display_food_info(food_item):
    """
    Display the nutritional info of a food item.
    """
    _, name, brand, calories, protein, carbs, fats, fiber = food_item
    print(f"\nName: {name}")
    print(f"Brand: {brand}")
    print(f"Calories (per 100g): {calories:.2f}")
    print(f"Protein (per 100g): {protein:.2f}")
    print(f"Carbs (per 100g): {carbs:.2f}")
    print(f"Fats (per 100g): {fats:.2f}")
    print(f"Fiber (per 100g): {fiber:.2f}")


def calculate_bmr(gender, weight, height, age):
    """
    Calculate BMR based on gender, weight (lbs), height (in), and age.
    """
    if gender.lower() == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif gender.lower() == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    else:
        raise ValueError("Invalid gender! Please enter male or female.")
    return bmr


def calculate_calories(bmr, activity_level):
    """
    Calculate daily calorie needs based on activity level.
    """
    activity_multipliers = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725
    }
    return bmr * activity_multipliers.get(activity_level.lower(), 1.2)


def calculate_macros(calories):
    """
    Calculate macronutrient distribution based on calorie intake.
    """
    protein = calories * 0.3 / 4  # 30% of calories to protein (1g = 4 cal)
    carbs = calories * 0.4 / 4    # 40% of calories to carbs (1g = 4 cal)
    fats = calories * 0.3 / 9     # 30% of calories to fats (1g = 9 cal)
    return protein, carbs, fats


def main():
    """
    Main function for the Calorie and Macro Tracker with multi-food logging.
    """
    print("Welcome to the Calorie and Macro Tracker!")
    
    # Collect user details
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight in lbs: "))
    height = float(input("Enter your height in inches: "))
    print("Activity levels: sedentary, lightly active, moderately active, very active")
    activity_level = input("Enter your activity level: ")

    # Calculate BMR and daily calories
    try:
        bmr = calculate_bmr(gender, weight, height, age)
        daily_calories = calculate_calories(bmr, activity_level)
        protein, carbs, fats = calculate_macros(daily_calories)

        print(f"\nHi {name}!")
        print(f"Your BMR is {bmr:.2f} calories/day.")
        print(f"To maintain your weight, you need approximately {daily_calories:.2f} calories/day.")
        print("Macronutrient breakdown (daily):")
        print(f"- Protein: {protein:.2f}g")
        print(f"- Carbs: {carbs:.2f}g")
        print(f"- Fats: {fats:.2f}g")

    except ValueError as e:
        print(f"Error: {e}")
        return

    # Initialize food log
    food_log = []

    # Food input and tracking
    while True:
        food_name = input("\nEnter the name of the food you ate (or 'exit' to quit): ").strip()
        if food_name.lower() == "exit":
            break

        # Search for food in the database
        results = search_food_in_database(food_name)
        if results:
            print(f"\nFound {len(results)} matching food(s) in the database:")
            for food in results:
                display_food_info(food)

                # Get amount consumed
                amount = float(input(f"How many grams of {food[1]} did you eat? "))

                # Calculate macros and calories for the amount consumed
                calories = (food[3] / 100) * amount
                protein = (food[4] / 100) * amount
                carbs = (food[5] / 100) * amount
                fats = (food[6] / 100) * amount

                # Add entry to food log
                food_log.append({
                    "name": food[1],
                    "amount": amount,
                    "calories": calories,
                    "protein": protein,
                    "carbs": carbs,
                    "fats": fats
                })

                # Display results
                print(f"\nFor {amount}g of {food[1]}:")
                print(f"- Calories: {calories:.2f}")
                print(f"- Protein: {protein:.2f}g")
                print(f"- Carbs: {carbs:.2f}g")
                print(f"- Fats: {fats:.2f}g")
        else:
            # Fetch from API if not found
            print(f"No results found for '{food_name}'. Fetching from Open Food Facts API...")
            fetch_and_store_food_data([food_name], page_size=5)
            print(f"Data for '{food_name}' has been fetched and stored. Try searching again.")

    # Summarize total macros
    print("\nSession Summary:")
    total_calories = sum(item["calories"] for item in food_log)
    total_protein = sum(item["protein"] for item in food_log)
    total_carbs = sum(item["carbs"] for item in food_log)
    total_fats = sum(item["fats"] for item in food_log)

    for item in food_log:
        print(f"{item['amount']}g of {item['name']}:")
        print(f"  - Calories: {item['calories']:.2f}")
        print(f"  - Protein: {item['protein']:.2f}g")
        print(f"  - Carbs: {item['carbs']:.2f}g")
        print(f"  - Fats: {item['fats']:.2f}g")

    print("\nTotal for the session:")
    print(f"- Calories: {total_calories:.2f}")
    print(f"- Protein: {total_protein:.2f}g")
    print(f"- Carbs: {total_carbs:.2f}g")
    print(f"- Fats: {total_fats:.2f}g")

    print("\nThank you for using the Calorie and Macro Tracker. Stay healthy!")


if __name__ == "__main__":
    main()
def main():
    """
    Main function for the Calorie and Macro Tracker with multi-food logging.
    """
    print("Welcome to the Calorie and Macro Tracker!")
    
    # Collect user details
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight in lbs: "))
    height = float(input("Enter your height in inches: "))
    print("Activity levels: sedentary, lightly active, moderately active, very active")
    activity_level = input("Enter your activity level: ")

    # Calculate BMR and daily calories
    try:
        bmr = calculate_bmr(gender, weight, height, age)
        daily_calories = calculate_calories(bmr, activity_level)
        protein, carbs, fats = calculate_macros(daily_calories)

        print(f"\nHi {name}!")
        print(f"Your BMR is {bmr:.2f} calories/day.")
        print(f"To maintain your weight, you need approximately {daily_calories:.2f} calories/day.")
        print("Macronutrient breakdown (daily):")
        print(f"- Protein: {protein:.2f}g")
        print(f"- Carbs: {carbs:.2f}g")
        print(f"- Fats: {fats:.2f}g")

    except ValueError as e:
        print(f"Error: {e}")
        return

    # Initialize food log
    food_log = []

    # Food input and tracking
    while True:
        food_name = input("\nEnter the name of the food you ate (or 'exit' to quit): ").strip()
        if food_name.lower() == "exit":
            break

        # Search for food in the database
        results = search_food_in_database(food_name)
        if results:
            print(f"\nFound {len(results)} matching food(s) in the database:")
            for food in results:
                display_food_info(food)

                # Get amount consumed
                amount = float(input(f"How many grams of {food[1]} did you eat? "))

                # Calculate macros and calories for the amount consumed
                calories = (food[3] / 100) * amount
                protein = (food[4] / 100) * amount
                carbs = (food[5] / 100) * amount
                fats = (food[6] / 100) * amount

                # Add entry to food log
                food_log.append({
                    "name": food[1],
                    "amount": amount,
                    "calories": calories,
                    "protein": protein,
                    "carbs": carbs,
                    "fats": fats
                })

                # Display results
                print(f"\nFor {amount}g of {food[1]}:")
                print(f"- Calories: {calories:.2f}")
                print(f"- Protein: {protein:.2f}g")
                print(f"- Carbs: {carbs:.2f}g")
                print(f"- Fats: {fats:.2f}g")
        else:
            # Fetch from API if not found
            print(f"No results found for '{food_name}'. Fetching from Open Food Facts API...")
            fetch_and_store_food_data([food_name], page_size=5)
            print(f"Data for '{food_name}' has been fetched and stored. Try searching again.")

    # Summarize total macros
    print("\nSession Summary:")
    total_calories = sum(item["calories"] for item in food_log)
    total_protein = sum(item["protein"] for item in food_log)
    total_carbs = sum(item["carbs"] for item in food_log)
    total_fats = sum(item["fats"] for item in food_log)

    for item in food_log:
        print(f"{item['amount']}g of {item['name']}:")
        print(f"  - Calories: {item['calories']:.2f}")
        print(f"  - Protein: {item['protein']:.2f}g")
        print(f"  - Carbs: {item['carbs']:.2f}g")
        print(f"  - Fats: {item['fats']:.2f}g")

    print("\nTotal for the session:")
    print(f"- Calories: {total_calories:.2f}")
    print(f"- Protein: {total_protein:.2f}g")
    print(f"- Carbs: {total_carbs:.2f}g")
    print(f"- Fats: {total_fats:.2f}g")

    print("\nThank you for using the Calorie and Macro Tracker. Stay healthy!")


if __name__ == "__main__":
    main()

