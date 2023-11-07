from django.shortcuts import render

# Create your views here.

tasks=["Diska", "Tvätta", "Dammsuga", "Spela", "Suga"]

def task(request):
    if request.method == "POST":
        test_write = request.POST.get("input")
        # print(test_write)
        tasks.append(test_write)
        
    return render(request,'add.html', {'tasks': tasks})