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


def dramaFilms(request):
    films = Movie.objects.filter(genre='Drama')
 
    return render(request, "genreList.html", {'films': films})

# def genreList(request): #TODO genre_id 

#     dramaFilms = Movie.objects.filter(genre='Drama')
#     actionFilms = Movie.objects.filter(genre='Action')
#     adventureFilms = Movie.objects.filter(genre='Adventure')
#     horrorFilms = Movie.objects.filter(genre='Horror')
#     biographyFilms = Movie.objects.filter(genre='Biography')

#     return render(request, "genreList.html", {'dramaFilms': dramaFilms, 'actionFilms': actionFilms, 'adventureFilms': adventureFilms, 'horrorFilms': horrorFilms, 'biographyFilms': biographyFilms})