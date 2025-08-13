from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def legacy(request):
    return render(request, 'legacy.html')

def services(request):
    return render(request, 'services.html')

def dealership(request):
    return render(request, 'dealership.html')

def store(request):
    return render(request, 'store.html')

def future(request):
    return render(request, 'future.html')