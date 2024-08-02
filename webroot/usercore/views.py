from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import registrationForm
from .models import User, businessid, subscriptions, subscriptionsid
from django.utils import timezone
import datetime
from django.utils.crypto import get_random_string
from django.db import transaction
from django.contrib.auth.models import Permission
# from django.contrib.contenttypes.models import ContentType
 
# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = registrationForm(request.POST)
        if form.is_valid():
            # form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username = username, password = password)
            # login(request, user)
            subID = subscriptionsid()
            busiID = businessid()
            permission = Permission.objects.get(codename='is_admin')
            subscription = subscriptions(subscriptionid = subID,
                                         businessid = busiID,
                                         start_date = timezone.now(),
                                         end_date = datetime.timedelta(days = 31)+timezone.now(),
                                         amount = 0,
                                         duration = datetime.timedelta(days=31),
                                         transaction_id = str(get_random_string(14).upper()),
                                         Discount = 0,
                                         payment_status = 'success',
                                         is_valid = True)
            
            with transaction.atomic():
                busiID.save()
                subID.save()
                subscription.save()
                user = User.objects.create_user(first_name=form.cleaned_data.get('first_name'),
                     username = form.cleaned_data.get('username'),
                     password = form.cleaned_data.get('password1'),
                     last_name = form.cleaned_data.get('last_name'),
                     gstin_Number = form.cleaned_data.get('gstin_Number'),
                     businessid=busiID,
                     email = form.cleaned_data.get('email'),
                     is_active = True,
                     admin_access = True,
                     businessName = form.cleaned_data.get('businessName'),
                     subscription = subID,
                     phone_contact = form.cleaned_data.get('phone_contact')
                     )
                # user.has_perm('is_admin')
                user.user_permissions.add(permission)
                user.save()

            return redirect('login')
        else:
            return render(request, 'registration.html', {'form':form})
    else:
        form = registrationForm()
        return render(request, 'registration.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html", {})