from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def layout(request):
    return render(request, "layout.html")