# Create your views here
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from serializers.serializer import Menu_Serializer

class MenuCategoryView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = Menu_Serializer