from rest_framework import serializers
from .models import CookingCategory

class CookingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingCategory
        fields = '__all__'


from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
