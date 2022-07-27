from dataclasses import fields
from rest_framework import serializers

from .models import Ingredient, Recipe, Direction


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            "id",
            "name",
            "recipe"
        )

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "category",
            "description",
            "image",
        )
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            "id",
            "body",
            "recipe"
        )
