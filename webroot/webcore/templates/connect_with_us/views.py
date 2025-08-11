from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from usercore.models import subscriptions, User, subscriptionsid
from django.utils import timezone
import uuid
from django.urls import reverse

@login_required
def connect(request):
    return render(request, 'connect_with_us/connect.html')