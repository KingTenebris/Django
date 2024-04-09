from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "index.html")

def signIn(request):
    if request.method == "POST":
            # [" name from input-name = '' ""]
            username = request.POST["username"] 
            password = request.POST["password"] 

            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/home")
            else:
                return render(request, "login.html", {"message": "User not found"})
    return render(request, "login.html")

def signOut(request):
     logout(request)
     return redirect("index")