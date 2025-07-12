from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    released_date = models.DateField()

