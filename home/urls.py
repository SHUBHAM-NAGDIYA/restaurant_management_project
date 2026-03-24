from django.urls import path
from .views import *

urlpatterns = [
    path('menu-categories/', MenuCategoryView.as_view(), name='menu-categories'),
]