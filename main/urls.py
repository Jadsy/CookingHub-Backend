from django.urls import path
from main import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view()),
    path('ingredients/', views.IngredientsList.as_view()),
    path('directions/', views.DirectionsList.as_view()),
]
