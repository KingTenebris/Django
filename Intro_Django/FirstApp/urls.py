from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('fisrtapp/', include("FisrtApp.urls"))
    path ("", views.home, name="home")
]