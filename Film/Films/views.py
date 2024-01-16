from django.shortcuts import render
from .models import Director, Movie

# Create your views here.
def directorsList(request):
    directors = Director.objects.all()
    return render(request, "authorList.html", {'directors': directors})

def filmsList(request):
    films = Movie.objects.all()
    return render(request, "filmsList.html", {'films': films})