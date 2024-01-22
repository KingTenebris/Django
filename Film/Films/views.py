from django.shortcuts import render
from .models import Director, Movie

# Create your views here.
def directorsList(request):
    directors = Director.objects.all()
    return render(request, "authorList.html", {'directors': directors})

def filmsList(request, director_id):
    director = Director.objects.get(id=director_id)

    films = Movie.objects.filter(director=director)
    return render(request, "filmsList.html", {'films': films, 'director':director})