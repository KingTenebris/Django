from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('addGame', views.addGame, name="addGame"),
    path('gameList', views.gameList, name="gameList"),
    path('gameInfo/<int:game_id>', views.gameInfo, name="gameInfo"),

    path('remove/<int:game_id>', views.removeGame, name = "removeGame")

]