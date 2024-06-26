from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.signIn, name="signIn"),
    path('logout/', views.signOut, name="signOut"),
]