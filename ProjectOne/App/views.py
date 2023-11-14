from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "home.html")

def calc(request):
    return render(request, "calculator.html")

def calcnumb(request, number):
    
    if request.method=="POST":
        data = request.POST.get("numb")
    # return render("calculator.html",{"data":data})
    return redirect(f"/home/calculator/{data}")

def forms(request):
    return render(request, "forms.html")

def toDo(request):
    return render(request, "toDo.html")


def layout(request):
    return render(request, "layout.html")
