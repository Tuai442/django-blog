from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class CookingCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cooking Categories"


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes', blank=True, null=True)  # Many-to-many field
    instructions = models.TextField(blank=True, null=True)
    cooking_time = models.PositiveIntegerField(blank=True, null=True)
    servings = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(CookingCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True, null=True)  # Many-to-many field
    image = models.ImageField(upload_to='recipe_images/', blank=True, null=True)  # New image field

    def __str__(self):
        return self.title


