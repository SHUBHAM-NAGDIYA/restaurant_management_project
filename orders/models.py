from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=100, unique=True)
    discount_percent = models.DecimalField(decimal_places=2)
    is_active = models.BooleanField(default=True)
    valid_from = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return self.code
