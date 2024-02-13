from django.shortcuts import render, redirect, HttpResponse
from .models import Director, Movie

# Create your views here.
def directorsList(request):
    directors = Director.objects.all()
    movie = Movie.objects.all()
    return render(request, "directorsList.html", {'directors': directors, 'movies':movie})

def filmsList(request, director_id):
    director = Director.objects.get(id=director_id)
    films = Movie.objects.filter(director=director)

    #TODO show all info about film (not only name)

    return render(request, "filmsList.html", {'films': films, 'director':director})


def genreMovies(request, genreName):
    selectedMovie=Movie.object.filter(genre=genreName)
    return render(request, "genreList.html", {"movies": selectedMovie, "genreName": genreName})
# Genre till filmer
def dramaFilms(request):
    films = Movie.objects.filter(genre='Drama') 
    return render(request, "genreList.html", {'films': films, 'genre': "Drama"})
def actionFilms(request):
    films = Movie.objects.filter(genre='Action')
    return render(request, "genreList.html", {'films': films, 'genre': "Action"})
def adventureFilms(request):
    films = Movie.objects.filter(genre='Adventure')
    return render(request, "genreList.html", {'films': films, 'genre': "Adventure"})
def horrorFilms(request):
    films = Movie.objects.filter(genre='Horror')
    return render(request, "genreList.html", {'films': films, 'genre': "Horror"})
def biographyFilms(request):
    films = Movie.objects.filter(genre='Biography')
    return render(request, "genreList.html", {'films': films, 'genre': "Biography"})


def addFilm(request):
    if request.method == "POST":
        directorInput = request.POST.get("director")

        titleInput = request.POST.get("title")
        yearInput = request.POST.get("year")
        ratingInput = request.POST.get("rating")
        genreInput = request.POST.get("genre")

        
        try:
            checkDirector = Director.objects.get(name=directorInput)
        except:
            return HttpResponse("Director not found", status=404)
        # Create and save a new film
        
        Movie.objects.create(title=titleInput, year=yearInput, rating=ratingInput, genre=genreInput, director=checkDirector)

        return redirect('/home/')
    
    else:
        return render(request, "addList.html")
