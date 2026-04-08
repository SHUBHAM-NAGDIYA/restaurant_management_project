#-------------------------------commit id---------------------------------------#

4905abbd01b19d444e30c38c2826369e11adcf18

#--------------------------------utils.py---------------------------------------#
import string
import secrets
from django.apps import apps

def generate_coupon_code(lenght=10):
    """
    Generate a unique alphnumeric coupon oce
    """
    characters = string.ascii_uppercase + string.digits

    Coupon = apps.get_model('orders', 'Coupon')

    while True:
        coupon_code = ''.join(secrets.choice(characters) for _ in range(length))

        #check uniqueness in DB
        if not Coupon.objects.filter(code=coupon_code).exists():
            return coupon_code

#-------------------------------------------------------------------------------#
