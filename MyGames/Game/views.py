from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.

# Function to render home page
def home(request):
    return render(request, "home.html")

# Function to create a game and send/post it in database
def addGame(request):
    # if-statement to check if user send information/request to server 
    if request.method == "POST": #! in ("...") is name from html
        gameName =  request.POST.get("gameName")
        gameYear =  request.POST.get("gameYear")
        gamePhase = request.POST.get("phases") 
        gameDeveloper = request.POST.get("developers")
        gamePlatform = request.POST.get("platforms")
        gameCategory = request.POST.get("categories")

        # Create a variable to store objects with foreignKey - foreignKey is not a string it's an object
        getPhases = Phase.objects.get(state = gamePhase)
        getPlatforms = Platform.objects.get(name = gamePlatform)
        getDevelopers = Developer.objects.get(name = gameDeveloper)
        getCategories = Category.objects.get(genre = gameCategory)
        
        # CRUD - create
        Game.objects.create(
            name = gameName, 
            year = gameYear, 
            phase = getPhases, 
            developer = getDevelopers, 
            platform = getPlatforms, 
            category = getCategories
            )
        
        # After user submitted a game, code will redirect him back to home page (to function that render home page)
        return redirect('/home')
    
    # else here to show all the option of select-option to user before he will choose anything
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

# Function to render/show a game list to user, of all game that he send/created to database
def gameList(request):
    # Taking all objects from each models
    games = Game.objects.all()
    phases = Phase.objects.all()
    developers = Developer.objects.all()
    categories = Category.objects.all()
    platforms = Platform.objects.all()

    dictionary = {
        "phases": phases,
        "developers": developers,
        "categories": categories,
        "platforms": platforms
    }

    # if-statement for a Filter
    if request.method == "POST":
        # HTML-input name = "..." for search
        checkName = request.POST.get("checkName")
        # name__icontains is for search method
        games = games.filter(name__icontains = checkName)

        # filtering all request of user, by checking phase, developer, category or platform separate or together
        gamePhase = request.POST.get("gamePhases")
        gameDeveloper = request.POST.get("gameDevelopers")
        gameCategory = request.POST.get("gameCategories")
        gamePlatform = request.POST.get("gamePlatforms") 
        
        # if-statement to run code if user chose not all
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

        if gameCategory != "all":
            category = Category.objects.get(genre = gameCategory)
            games = games.filter(category = category)
            # Adding key valuer to dictionary 
            dictionary["category"] = category

        if gamePlatform != "all":
            platform = platform.objects.get(name = gamePlatform)
            games = games.filter(platform = platform)
            # Adding key valuer to dictionary 
            dictionary["platform"] = platform
        
    # Update key value in dictionary (upper)
    dictionary["games"] = games
    # render additional information in dictionary if user chose to filter anything 
    return render(request, "gameList.html", dictionary)

# Function to show information about game
def gameInfo(request, game_id):

    # bool-checker to see if a user want to see information about game or edit it
    checkEdit = False

    # get an id of each game separated
    game = Game.objects.get(id=game_id)

    dictionary = {
        "game": game, 
        "checkEdit":checkEdit
    }

    return render(request, "gameInfo.html", dictionary)

# Function to edit game
# "game_id" an argument to use as a path in web
def editGame(request, game_id):

    # The same method as in gameInfo
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
        
        # Changing value, by what user edit
        game.name = gameName
        game.year = gameYear
        game.phase = getPhases
        game.platform = getPlatforms
        game.developer = getDevelopers
        game.category = getCategories

        # save or an update method...
        game.save() 

        # redirect using name from urls.py
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

# Function to remove game from database and html show-list
def removeGame(request, game_id):
    
    # The same method with id to delete each specific game
    game = Game.objects.get(id=game_id)

    # CRUD - delete
    game.delete()

    # redirect back to function gameList to stay on the same page after removing game 
    return redirect("gameList")
