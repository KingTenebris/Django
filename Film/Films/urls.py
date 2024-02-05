from django.contrib import admin
from django.urls import path
from . import views
from .views import directorsList, filmsList

urlpatterns = [
    path('', views.directorsList, name="directorsList"),
    path('<int:director_id>', views.filmsList, name="filmsList"),

    path('genre/<str:genre_name>', views.genre_movies, name="genre_movies"),

    path('drama/', views.dramaFilms, name="dramaFilms"),
    path('action/', views.actionFilms, name="actionFilms"),
    path('adventure/', views.adventureFilms, name="adventureFilms"),
    path('horror/', views.horrorFilms, name="horrorFilms"),
    path('biography/', views.biographyFilms, name="biographyFilms"),
]
