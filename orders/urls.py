from django.urls import path
from .views import *

urlpatterns = [
    path( 'CouponValidationView/',CouponValidationView.as_view(), name='CouponValidationView' )
    
]