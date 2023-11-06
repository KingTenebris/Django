from django.shortcuts import render

# Create your views here.
def home(request):
    rubrik = "Hello, this is home"
    text = "Some kind of text"
    return render(request, "index.html", {"rubrik":rubrik, "text":text})

def lista(request):
    rubrik = "This is my List:"
    lista = ["car", "game", "tv-show"]
    return render(request, "index.html", {"rubrik":rubrik, "lista":lista})