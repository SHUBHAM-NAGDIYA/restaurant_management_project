from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_featured = models.BooleanField(default=False)

class Restaurant(models.Model):
    has_delivery = models.BooleanField(default=False)
    pass