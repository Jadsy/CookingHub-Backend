from distutils.command.upload import upload
from email.mime import image
import tempfile
from time import time
from unicodedata import category, name
from django.db import models
import uuid

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=120, null=True, blank=True)
    category = models.OneToOneField(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    prep_time = models.FloatField(null=True, blank=True)
    servings = models.FloatField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    ingredients = models.CharField(max_length=2000, null=True, blank=True)
    instructions = models.CharField(max_length=2000, null=True, blank=True)
    is_public = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.name


