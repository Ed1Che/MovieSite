from django.db import models

# Create your models here.
class Suggestion (models.Model):
    Title = models.CharField(max_length=100, unique=True)
    Director= models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

