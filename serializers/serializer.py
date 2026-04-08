from rest_framework import serializers
from home.models import MenuCategory

class Menu_Serializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ["name"]
