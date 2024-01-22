from django.contrib import admin
from django.urls import path
from . import views
from .views import directorsList, filmsList

urlpatterns = [
    path('<int:director_id>', views.filmsList, name="filmsList"),
    path('', views.directorsList, name="directorsList"),
]
