from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # name can be used to redirect
    # views.name if the name of function in views.py
    path('', views.home, name="home"),
    path('addGame', views.addGame, name="addGame"),
    path('gameList', views.gameList, name="gameList"),
    path('gameInfo/<int:game_id>', views.gameInfo, name="gameInfo"),
    # is not a specific url, more like back-end function that will work, but not appear to user 
    path('remove/<int:game_id>', views.removeGame, name = "removeGame"),
    path('gameInfo/<int:game_id>/edit', views.editGame, name="editGame"),
]