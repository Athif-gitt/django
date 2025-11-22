from django.db import models

class Geek(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

