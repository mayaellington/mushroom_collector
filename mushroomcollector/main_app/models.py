from django.db import models

# Create your models here.
class Mushroom(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    season = models.CharField(max_length=100)
    edibility = models.CharField(max_length=100)

    def __str__(self):
        return self.name