from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def logIn(request):
    return render(request, "login.html")