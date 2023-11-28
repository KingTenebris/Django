from django.shortcuts import render, redirect

# Create your views here.
def calculator(request):
    return render(request, 'calculator.html')

def calcNumber(request, number):
    numbers = []
    for i in range(1,11):
        a = number * i
        numbers.append(a)
    return render(request, "calculator.html", {"number":number, "numbers":numbers})

def number(request):
    if request.method == "POST":
        numb = request.POST.get("number")
    return redirect("calcNumber", numb)