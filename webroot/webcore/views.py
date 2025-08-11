from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from usercore.models import subscriptions, User, subscriptionsid
from django.utils import timezone
import uuid
from django.urls import reverse
# Create your views here.

@never_cache
@login_required(redirect_field_name='user/login')
def index(request):
    subscription_data = subscriptions.objects.get(subscriptionid=User.objects.get(username=request.user).subscription).end_date
    timenow = timezone.now()
    if  subscription_data > timenow:
        return render(request, 'index.html')
    else:
        token = uuid.uuid4()
        if 'redirect_tokens' not in request.session:
            request.session['redirect_token']={}
        redirect.session['redirect_token'][token] = True
        redirect.session.save()
        return redirect(reverse('subscription')+f'?token={token}')

@login_required
@never_cache
def stock(request):
    
    return render(request, 'stock.html')

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

@login_required
def list_template(request):
    return render(request, 'list_template.html')
@login_required
def profile(request):
    return render(request, 'profile.html')

