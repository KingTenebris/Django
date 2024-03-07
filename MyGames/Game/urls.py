from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('AddGame', views.addGame, name="addGame"),
    path('ListOfGames', views.games, name="games"),
]