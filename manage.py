#-------------------------------commit id---------------------------------------#

c7bad7ee6e08fb44c4b3fc2d6ffb6981d66cbf59

#--------------------------------Menu Caegory View End Point-----------------------------------#
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from serializers.serializer import Menu_Serializer

class MenuCategoryView(ListAPIView):
    query_set = MenuCategory.objects.all()
    serializer_class = Menu_Serializer


#--------------------------------Menu_Serializer--------------------------------#

from rest_framework import serializers
from home.models import MenuCategory

class Menu_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['name']

#-------------------------------URL's-------------------------------------------#

from django.urls import path
from .views import *

urlpatterns = [
    path('menu-categories/', MenuCategoryView.as_view(), name = 'menu-categories')
    ]

#-------------------------------------------------------------------------------#










