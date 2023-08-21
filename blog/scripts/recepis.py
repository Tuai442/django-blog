from core.models import CookingCategory, Recipe
import random

# Assume you have existing CookingCategory instances
categories = CookingCategory.objects.all()

# Sample recipe data
sample_recipes = [
    {
        "title": "Spaghetti Carbonara",
        "description": "A classic Italian pasta dish...",
        "ingredients": "200g spaghetti, 100g pancetta...",
        "instructions": "1. Cook the spaghetti...",
        "cooking_time": 30,
        "servings": 4,
        "category": categories[0],
        "image": "spaghetti.jpg"
    },
    {
        "title": "Pizza Marherita",
        "description": "A quick and delicious stir-fry...",
        "ingredients": "250g chicken breast, assorted vegetables...",
        "instructions": "1. Cut the chicken into strips...",
        "cooking_time": 20,
        "servings": 2,
        "category": categories[1],
        "image": "pizza_marherita.jpg"

    },
    # Add more sample recipe data
]

# Insert the sample recipe data into the database
for recipe_data in sample_recipes:
    recipe = Recipe.objects.create(
        title=recipe_data["title"],
        description=recipe_data["description"],
        ingredients=recipe_data["ingredients"],
        instructions=recipe_data["instructions"],
        cooking_time=recipe_data["cooking_time"],
        servings=recipe_data["servings"],
        category=recipe_data["category"],
        image=recipe_data["image"]
    )
    print(f"Created recipe: {recipe.title} - {recipe.category}")
