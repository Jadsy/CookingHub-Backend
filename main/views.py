import imp
from django.shortcuts import render
from .models import Category, Direction, Ingredient, Recipe
from .serializers import IngredientSerializer, DirectionSerializer, RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class RecipeList(APIView):
    def get(self, request):
        category = request.GET.get("category")
        if id:
            recipes = Recipe.objects.filter(category=category)
        else:
            recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        recipe_data = request.data
        new_recipe = Recipe.objects.create(
                name=recipe_data['name'],
                category=recipe_data['category'],
                description=recipe_data['description'],
                image=recipe_data['image'],
            )
        serialized_obj = RecipeSerializer(new_recipe)
        return Response(serialized_obj.data)


class IngredientsList(APIView):
    def get(self, request):
        recipeId = request.GET.get("recipeId")
        ingredients = Ingredient.objects.filter(recipe=recipeId)
        serializer = IngredientSerializer(ingredients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        ingredient_data = request.data
        new_ingredient = Ingredient.objects.create(
                name=ingredient_data['name'],
                recipe=Recipe.objects.get(ingredient_data['recipe']),
            )
        serialized_obj = IngredientSerializer(new_ingredient)
        return Response(serialized_obj.data)

        
class DirectionsList(APIView):
    def get(self, request):
        recipeId = request.GET.get("recipeId")
        directions = Direction.objects.filter(recipe=recipeId)
        serializer = DirectionSerializer(directions, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        direction_data = request.data
        new_direction = Direction.objects.create(
                name=direction_data['body'],
                recipe=Recipe.objects.get(direction_data['recipe']),
            )
        serialized_obj = DirectionSerializer(new_direction)
        return Response(serialized_obj.data)