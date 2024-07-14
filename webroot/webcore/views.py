from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        "name" : 6333,
        "user" : "user",
    }
    return render(request, 'index.html', context=context)

def stock(request):
    return render(request, 'stock.html')

def workshop(request):
    return render(request, 'workshop.html')

def service(request):
    return render(request, 'service.html')

def insurance(request):
    return render(request, 'insurance.html')

def department(request):
    return render(request, 'department.html')

def signout(request):
    return render(request, 'signout.html')

def stockadd(request):
    return render(request, 'stock_add.html')