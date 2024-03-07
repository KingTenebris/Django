from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    return render(request, "home.html")

def addGame(request):
    if request.method == "POST": #! in ("...") is name from html
        gameName = request.POST.get ("gameName")
        gameYear = request.POST.get ("gameYear")
        gamePhase = request.POST.get ("phases") 
        gameDeveloper = request.POST.get ("developers")
        gamePlatform = request.POST.get ("platforms")
        gameCategory = request.POST.get ("categories")
    
    else:
        gamePhase = Phase.objects.all()
        gameDeveloper = Developer.objects.all()
        gamePlatform = Platform.objects.all()
        gameCategory = Category.objects.all()

    dictionary = {
        "phases":       gamePhase,
        "developers":   gameDeveloper,
        "platforms":    gamePlatform,
        "categories":   gameCategory
    }
        

    # dictionary                              "key (to html)" : variable (here)
    return render(request, "addGame.html", dictionary)

def games(request):
    return render(request, "games.html")