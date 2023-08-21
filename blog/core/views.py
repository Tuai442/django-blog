from django.shortcuts import render, redirect
from core.models import CookingCategory, Recipe, User, Ingredient
from core.serializers import CookingCategorySerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.forms import RegistrationForm, AddRecipeForm, LoginForm
from django.http import JsonResponse
import json

def home(request, category_id=None):
    print(f"category_id: {category_id}")
    categories = CookingCategory.objects.all()

    recepies = []
    if category_id:
        recepies = Recipe.objects.filter(category__id=category_id)
    else:
        recepies = Recipe.objects.filter(category=categories[0])
    
    context = {
        'cooking_categories': categories,
        'cooking_recepies': recepies,
    }
    
    return render(request, 'home.html', context)

def add_recipe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print(f"data: {data}")
            title = data.get('title')
            category_id = data.get('category')
            description = data.get('description')
            image = data.get('image')
            ingredients = data.get('ingredients')

            category = CookingCategory.objects.get(id=category_id)
            print(f"category: {category}")
            new_recipe = Recipe(title=title, category=category, description=description, image=image)
            new_recipe.save()

            for ingredient_data in ingredients:
                print(f"ingredient_data: {ingredient_data}")
                ingredient_name = ingredient_data.get('name')
                ingredient_amount = ingredient_data.get('amount')
                
                # Check if the ingredient already exists in the database
                ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
                
                # Add the ingredient to the recipe's ingredients using the ManyToManyField
                new_recipe.ingredients.add(ingredient, through_defaults={'amount': ingredient_amount})

            print(f"new_recipe: {new_recipe}")
            return JsonResponse({"message": "Recipe added successfully"})
        
        except Exception as e:
            print(f"error: {e}")
            return JsonResponse({"error": str(e)}, status=400)

    categories = CookingCategory.objects.all()
    context = {
        'cooking_categories': categories,
    }
    return render(request, 'add_recipe.html', context)

def recipe_details(request):
    recipe_id = request.GET.get('recipe_id')
    print(f"recipe_id: {recipe_id}")
    recipe = Recipe.objects.get(id=recipe_id)
    context = {
        'recipe': recipe,
    }
    return render(request, 'recipe_details.html', context)


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
def registration_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(f"form: {request.POST}")
        if form.is_valid():
            print(f"form: {form.cleaned_data}")
            form.save()
            return redirect('login')  
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def logout_page(request):
    logout(request)
    return redirect('home')