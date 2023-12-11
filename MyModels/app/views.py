from django.shortcuts import render
from .models import Person

# Create your views here.

def index(request):
    j = Person(name="John", age=10)
    g = Person(name="Garry", age=12)

    j.save()
    g.save()

    persons = Person.objects.all()
    return render(request, "index.html", {"persons":persons})

