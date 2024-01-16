from django.contrib import admin
from django.urls import path
from . import views
from .views import directorsList, filmsList

urlpatterns = [
    path('directors/', views.directorsList, name="directorsList"),
]
