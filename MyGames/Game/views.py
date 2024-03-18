from django.shortcuts import render, redirect, HttpResponse
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
    

        try:
            checkPhase = Phase.objects.get (name = gamePhase) #name???
        except:
            return HttpResponse("Something not found", state=404)
        
        Games.objects.create(name = gameName, year = gameYear, phase = checkPhase)

        return redirect('/home')
    
        #TODO try except method with all selections 


    else:
        gamePhase = Phase.objects.all()
        gameDeveloper = Developer.objects.all()
        gamePlatform = Platform.objects.all()
        gameCategory = Category.objects.all()

    # dictionary - "key (to html)" : variable (here)
    dictionary = {
        "phases":       gamePhase,
        "developers":   gameDeveloper,
        "platforms":    gamePlatform,
        "categories":   gameCategory
    }
        
    return render(request, "addGame.html", dictionary)

def games(request):
    return render(request, "games.html")