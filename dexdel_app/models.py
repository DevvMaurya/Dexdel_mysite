from django.db import models

# Create your models here. DataBase schema
class ImageModel(models.Model):
    imageName = models.CharField(max_length=255,unique=True)
    image = models.BinaryField()

class SearchHistory(models.Model):
    ask = models.CharField(max_length = 255)