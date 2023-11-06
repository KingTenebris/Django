from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    # path('lista/', views.lista ,name="lista"),
    path('layout/', views.layout, name="layout"),
]