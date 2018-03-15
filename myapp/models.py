from django.db import models

# Create your models here.
class Question(models.Model):
    name=models.CharField(max_length=255)
    age=models.CharField(max_length=10)
    height=models.CharField(max_length=15)
    image = models.FileField()