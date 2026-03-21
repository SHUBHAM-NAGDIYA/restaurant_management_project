from django.db import models

# Create your models here.

class OrderStatus(models.Model):
    name = models.CharField(max_length=100,unique=True)
    
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
