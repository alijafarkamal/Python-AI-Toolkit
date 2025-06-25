import requests

def nutrition_analysis():
    app_id = "c5340a66"  # Replace with your Edamam App ID
    app_key = "d34c13b8a2f1620fb0bb058a5fe8534f"  # Replace with your Edamam App Key
    ingredient = input("Enter the ingredient for nutrition analysis: ")

    url = "https://api.edamam.com/api/nutrition-data"
    params = {
        "app_id": app_id,
        "app_key": app_key,
        "ingr": ingredient
    }
    response = requests.get(url, params=params)

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code != 200:
        print("Failed to fetch nutrition data. Please try again.")
        return
    
    nutrition_data = response.json()
    if not nutrition_data:
        print("No nutrition data found.")
        return

    print("\nNutrition Analysis:")
    print(f"Calories: {nutrition_data.get('calories', 'N/A')} kcal")
    print(f"Total Weight: {nutrition_data.get('totalWeight', 'N/A')} g")
    print("Nutrients:")
    for nutrient, info in nutrition_data.get('totalNutrients', {}).items():
        print(f"  {info['label']}: {info['quantity']:.2f} {info['unit']}")

nutrition_analysis()