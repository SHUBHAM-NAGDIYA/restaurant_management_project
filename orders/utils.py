# orders/utils.py

import string
import secrets
from django.apps import apps


def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code.
    """

    characters = string.ascii_uppercase + string.digits

    Coupon = apps.get_model('orders', 'Coupon')  # avoids circular import

    while True:
        coupon_code = ''.join(secrets.choice(characters) for _ in range(length))

        # Check uniqueness in DB
        if not Coupon.objects.filter(code=coupon_code).exists():
            return coupon_code