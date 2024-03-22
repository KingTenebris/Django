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
            # on the left side "name" from models.py
            checkPhase = Phase.objects.get (state = gamePhase) 
            checkDeveloper = Developer.objects.get (name = gameDeveloper)
            checkPlatform = Platform.objects.get (name = gamePlatform)
            checkCategory = Category.objects.get (genre = gameCategory)
        except:
            return HttpResponse("Something not found", state=404)
        
        
        Game.objects.create(name = gameName, year = gameYear, phase = checkPhase, developer = checkDeveloper, platform = checkPlatform, category = checkCategory)

        return redirect('/home')
    
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

def gameList(request):
    games = Game.objects.all()
    return render(request, "gameList.html", {"games": games})

def gameInfo(request, game_id):
    checkEdit = False
    game = Game.objects.get(id=game_id)
    return render(request, "gameInfo.html", {"game": game, "checkEdit":checkEdit})

def editGame(request, game_id):
    game = Game.objects.get(id=game_id)
    checkEdit = True
    phases = Phase.objects.all()
    platforms = Platform.objects.all()
    developers = Developer.objects.all()
    categories = Category.objects.all()

    dictionary = {
        "game": game,
        "checkEdit": checkEdit,
        "phases": phases,
        "platforms": platforms,
        "developers": developers,
        "categories": categories
    }
    
    return render(request, "gameInfo.html", dictionary)

def removeGame(request, game_id):
    game = Game.objects.get(id=game_id)
    game.delete()
    return redirect("gameList")