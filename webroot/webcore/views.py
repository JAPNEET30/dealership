from django.shortcuts import render
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from usercore.models import subscriptions

# Create your views here.

@never_cache
@login_required(redirect_field_name='user/login')
def index(request):
    context={
        "name" : 6333,
        "user" : request.user,
        "permissions":'',
    }
    return render(request, 'index.html', context=context)

@login_required
@never_cache
def stock(request):
    
    return render(request, 'stock.html')

@login_required
@never_cache
def track(request):
    
    return render(request, 'track.html')

@login_required
@never_cache
def workshop(request):
    return render(request, 'workshop.html')

@login_required
@never_cache
def service(request):
    return render(request, 'service.html')

@login_required
@never_cache
def insurance(request):
    return render(request, 'insurance.html')

@login_required
def department(request):
    return render(request, 'department.html')

@never_cache
@login_required
def logout_view(request):
    return render(request, 'logout.html')

@never_cache
@login_required
def subscription(request):
    return render(request, 'subscription.html')