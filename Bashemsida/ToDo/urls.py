from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shoplist, name="shoplist"),
    
    path('doneShop', views.doneShop, name="doneShop"),
    path('removeItem', views.removeItem, name="removeItem"),
]