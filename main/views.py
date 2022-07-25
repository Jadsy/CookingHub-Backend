import imp
from django.shortcuts import render
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class RecipeList(APIView):
    def get(self, request):
        id = request.GET.get("id")
        if id:
            recipes = Recipe.objects.filter(id=id)
        else:
            recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)


class CategoryList(APIView):
    def get(self, request):
        categories = Recipe.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)