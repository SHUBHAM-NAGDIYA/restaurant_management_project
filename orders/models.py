from django.db import models

# Order models here.

# OrderStaus
class OrderStatus(models.Model):
    name = models.CharField(max_length=100,unique=True)

# Orders    
class Order(models.Model):
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, null=True)
