from django.urls import path
from .views import *

urlpatterns = [
    path( 'RetrieveAPIView/',RetrieveAPIView, name='RetrieveAPIView' )
    
]