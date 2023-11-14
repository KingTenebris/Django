from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Calculator 
    path("calculator/", views.calc, name="calc"),

    path("calcnumb/<int:number>", views.calcnumb, name="calcnumb"),
    # Forms
    path("forms/", views.forms, name="forms"),
    # To-Do List
    path("toDo/", views.toDo, name="toDo"),

    path("layout/", views.layout, name="layout")
]