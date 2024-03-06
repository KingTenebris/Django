from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def addGame(request):
    if request.method == "POST":
        gameName = request.POST.get ("gameName")
        gameYear = request.POST.get ("gameYear")
        gamePhase = request.POST.get ("gamePhase")
        gameDeveloper = request.POST.get ("gameDeveloper")
        gamePlatform = request.POST.get ("gamePlatform")
        gameCategory = request.POST.get ("gameCategory")

    return render(request, "addGame.html")