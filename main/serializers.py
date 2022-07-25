from dataclasses import fields
from rest_framework import serializers

from .models import Category, Recipe


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = (
            "id",
            "name",
            "category",
            "prep_time",
            "servings",
            "image",
            "ingredients",
            "instructions",
            "is_public"
        )