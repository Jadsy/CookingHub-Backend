from distutils.command.upload import upload
from email.mime import image
from time import time
from unicodedata import category, name
from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, null=True, blank=True)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, null=True, blank=True)

class Direction(models.Model):
    id = models.AutoField(primary_key=True)
    body = models.CharField(max_length=120, null=True, blank=True)
    recipe = models.OneToOneField(Recipe, on_delete=models.CASCADE, null=True, blank=True)
