from django.db import models

class Geek(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
class Author(models.Model):
    name = models.CharField(max_length= 200)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Movie(models.Model):
    title = models.CharField(max_length= 100)
    genre = models.CharField(max_length= 100)
    rating = models.FloatField()
    release_year = models.IntegerField()

    def __str__(self):
        return self.title

