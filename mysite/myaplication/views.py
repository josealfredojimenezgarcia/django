from django.shortcuts import render

# Create your views here.
def index(request):
    print("estoy renderizando un index")
    return render(request, 'myaplication\index.html', {})

def index1(request):
    print("estoy renderizando un index1")
    return render(request, 'myaplication\index1.html', {})

def index2(request):
    print("estoy renderizando un index2")
    return render(request, 'myaplication\index2.html', {})

def index3(request):
    print("estoy renderizando un index3")
    return render(request, 'myaplication\index3.html', {})

def index4(request):
    print("estoy renderizando un index4")
    return render(request, 'myaplication\index4.html', {})

def index5(request):
    print("estoy renderizando un index5")
    return render(request, 'myaplication\index5.html', {})

def django1(request):
    print("estoy renderizando un django")
    return render(request, 'myaplication\django1.html', {})
