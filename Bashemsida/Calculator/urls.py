from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calculator, name="calculator"),

    path('<int:number>', views.calcNumber, name="calcNumber"),

    path('number', views.number, name="number")
]