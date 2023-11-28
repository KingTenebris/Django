from django.shortcuts import render, redirect

# Create your views here.
def forms(request):
    return render(request, 'forms.html')

def doneForms(request):
    if request.method == "POST":
        qOne = request.POST.get("q1")
        qTwo = request.POST.get("q2")
        qTree = request.POST.get("q3")
        qFour = request.POST.get("q4")
    return render(request, "forms2.html", {"qOne":qOne, "qTwo":qTwo, "qTree":qTree, "qFour":qFour})