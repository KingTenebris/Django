from django.shortcuts import render, redirect

# Create your views here.
fList = []
cList = []
eList = []
oList = []

def shoplist(request):

    dictionary = {}
    # Food list
    try: 
        if fList[0]:
            dictionary["fList"] = fList
    except:
        pass
    
    # Cleaning list
    try: 
        if cList[0]:
            dictionary["cList"] = cList
    except:
        pass
    # Electronic list
    try: 
        if eList[0]:
            dictionary["eList"] = eList
    except:
        pass
    # Other list
    try: 
        if oList[0]:
            dictionary["oList"] = oList
    except:
        pass

    # Render everything dictionary has
    return render(request, 'shoplist.html', dictionary)

def doneShop(request):
    if request.method == "POST":
        userInput = request.POST.get("buy")
        l = request.POST.get("categories")
        if l == "Food":
            fList.append(userInput)
        elif l == "Cleaning":
            cList.append(userInput)
        elif l == "Electronic":
            eList.append(userInput)
        elif l == "Other":
            oList.append(userInput)

    return redirect('shoplist') 

def removeItem(request): 
    if request.method == "POST":
        for f in fList:
            fIndex = fList.index(f) + 1
            rm = request.POST.get(f"{fIndex}{f}")
            if rm == (f"{fIndex}{f}"):
                fList.remove(f"{f}")

        for c in cList:
            cIndex = cList.index(c) + 1
            rm = request.POST.get(f"{cIndex}{c}")
            if rm == (f"{cIndex}{c}"):
                cList.remove(f"{c}")

        for e in eList:
            eIndex = eList.index(e) + 1
            rm = request.POST.get(f"{eIndex}{e}")
            if rm == (f"{eIndex}{e}"):
                eList.remove(f"{e}")

        for o in oList:
            oIndex = oList.index(o) + 1
            rm = request.POST.get(f"{oIndex}{o}")
            if rm == (f"{oIndex}{o}"):
                oList.remove(f"{o}")
                
    return redirect('shoplist')

        
