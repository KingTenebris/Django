from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, "home.html")



def calc(request):
    return render(request, "calculator.html")

def calcnumb(request):
    if request.method=="POST":
        number = request.POST.get("numb")
    return redirect(f"/home/calculator/{number}")

def results(request, number):

    summa = number * 2

    return render(request, "calculator.html", {"number":number, "summa":summa})








def forms(request):
    return render(request, "forms.html")

def toDo(request):
    return render(request, "toDo.html")


def layout(request):
    return render(request, "layout.html")
