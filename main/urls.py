from django.urls import path
from main import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view()),
    path('categories/', views.CategoryList.as_view())
]
