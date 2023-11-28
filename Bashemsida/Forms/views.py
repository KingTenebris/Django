from django.shortcuts import render, redirect

# Create your views here.
def forms(request):
    return render(request, 'forms.html')