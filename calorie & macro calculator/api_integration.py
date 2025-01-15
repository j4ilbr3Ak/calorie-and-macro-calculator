import requests
from database import insert_food_item

def fetch_and_store_food_data(query_list, page_size=5):
    """
    Fetch food data from Open Food Facts API and store it in the database.
    """
    url = "https://world.openfoodfacts.org/cgi/search.pl"

    for query in query_list:
        params = {
            "search_terms": query,
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "page_size": page_size
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            products = response.json().get("products", [])
            print(f"Fetched {len(products)} products for '{query}'.")

            for product in products:
                name = product.get("product_name", "Unknown")
                brand = product.get("brands", "Unknown")
                nutrients = product.get("nutriments", {})

                calories = nutrients.get("energy-kcal_100g", 0)
                protein = nutrients.get("proteins_100g", 0)
                carbs = nutrients.get("carbohydrates_100g", 0)
                fats = nutrients.get("fat_100g", 0)
                fiber = nutrients.get("fiber_100g", 0)

                # Insert into the database
                insert_food_item(name, brand, calories, protein, carbs, fats, fiber)
        else:
            print(f"API request failed for '{query}' with status code: {response.status_code}")
