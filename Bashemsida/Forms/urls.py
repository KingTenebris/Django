from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms, name="forms"),

    path('done', views.doneForms, name="doneForms"),
]