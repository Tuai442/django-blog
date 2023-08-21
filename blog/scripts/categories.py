from core.models import CookingCategory  # Replace 'your_app_name' with the actual app name

def run():
    category_data = [
        {"name": "Italian Cuisine", "description": "Delicious dishes from Italy."},
        {"name": "Asian Fusion", "description": "Blend of Asian flavors."},
        {"name": "Healthy Eating", "description": "Nutritious and balanced meals."},
        # Add more categories here
    ]

    for data in category_data:
        cooking_category = CookingCategory(name=data["name"], description=data["description"])
        cooking_category.save()

    print(f"{len(category_data)} cooking categories generated.")
