from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, "home.html")

def addGame(request):
    if request.method == "POST": #! in ("...") is name from html
        gameName =  request.POST.get("gameName")
        gameYear =  request.POST.get("gameYear")
        gamePhase = request.POST.get("phases") 
        gameDeveloper = request.POST.get("developers")
        gamePlatform = request.POST.get("platforms")
        gameCategory = request.POST.get("categories")

        # Create a variable to store objects with foreignKey
        getPhases = Phase.objects.get(state = gamePhase)
        getPlatforms = Platform.objects.get(name = gamePlatform)
        getDevelopers = Developer.objects.get(name = gameDeveloper)
        getCategories = Category.objects.get(genre = gameCategory)
        
        Game.objects.create(name = gameName, year = gameYear, phase = getPhases, developer = getDevelopers, platform = getPlatforms, category = getCategories)

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
    phases = Phase.objects.all()
    developers = Developer.objects.all()

    dictionary = {
        "phases": phases,
        "developers": developers
    }

    # Filter:
    if request.method == "POST":
        # HTML select name = "..."
        checkName = request.POST.get("checkName")
        # name__icontains is for search method
        games = games.filter(name__icontains = checkName)

        gamePhase = request.POST.get("gamePhases")
        gameDeveloper = request.POST.get("gameDevelopers") 
        
        if  gamePhase != "all":
            phase = Phase.objects.get(state = gamePhase)
            games = games.filter(phase = phase)
            # Adding key valuer to dictionary 
            dictionary["phase"] = phase

        if  gameDeveloper != "all":
            developer = Developer.objects.get(name = gameDeveloper)
            games = games.filter(developer = developer)
            # Adding key valuer to dictionary 
            dictionary["developer"] = developer
        

    # Update key value in dictionary (upper)
    dictionary["games"] = games
    

    return render(request, "gameList.html", dictionary)

def gameInfo(request, game_id):
    checkEdit = False
    game = Game.objects.get(id=game_id)

    dictionary = {
        "game": game, 
        "checkEdit":checkEdit
    }

    return render(request, "gameInfo.html", dictionary)
# "game_id" using as a path in web
def editGame(request, game_id):

    game = Game.objects.get(id=game_id)
    checkEdit = True

    # Update game info 
    if request.method == "POST": #! in ("...") is name from html
        gameName = request.POST.get ("gameName")
        gameYear = request.POST.get ("gameYear")
        gamePhase = request.POST.get ("gamePhases") 
        gamePlatform = request.POST.get ("gamePlatforms")
        gameDeveloper = request.POST.get ("gameDevelopers")
        gameCategory = request.POST.get ("gameCategories")

        # Create a variable to store objects with foreignKey
        getPhases = Phase.objects.get(state = gamePhase)
        getPlatforms = Platform.objects.get(name = gamePlatform)
        getDevelopers = Developer.objects.get(name = gameDeveloper)
        getCategories = Category.objects.get(genre = gameCategory)
        
        # Changing value
        game.name = gameName
        game.year = gameYear
        game.phase = getPhases
        game.platform = getPlatforms
        game.developer = getDevelopers
        game.category = getCategories

        game.save() 

        # Use name from urls.py
        return redirect('gameInfo', game_id)

    # Open objects to use them in dictionary to create a for-loop, to see all objects from each base - in template
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
