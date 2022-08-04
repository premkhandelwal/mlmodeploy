from django.db import models

# Create your models here.
class Predict(models.Model):
    sepal_length = models.PositiveIntegerField()
    sepal_width = models.PositiveIntegerField()
    petal_length = models.PositiveIntegerField()
    petal_width = models.PositiveIntegerField()