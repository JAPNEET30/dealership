from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import registrationForm
from .models import User, businessid, subscriptions, subscriptionsid
from django.utils import timezone
import datetime
from django.utils.crypto import get_random_string
from django.db import transaction
from django.contrib.auth.models import Permission
from django.http import Http404

# from django.contrib.contenttypes.models import ContentType
import json
 
# Views
@login_required
def home(request):
    return render(request, "registration/success.html", {})
 
def register(request):
    form = registrationForm(request.POST)
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        
        if form.is_valid():
            subID = subscriptionsid()
            busiID = businessid()
            permission = Permission.objects.get(codename='is_admin')
            subscription = subscriptions(subscriptionid = subID,
                                         businessid = busiID,
                                         start_date = timezone.now(),
                                         end_date = datetime.timedelta(days = 1)+timezone.now(),
                                         amount = 0,
                                         duration = datetime.timedelta(days=1),
                                         transaction_id = str(get_random_string(14).upper()),
                                         Discount = 0,
                                         payment_status = 'pass',
                                         is_valid = True)
            
            with transaction.atomic():
                busiID.save()
                subID.save()
                subscription.save()
                user = User.objects.create_user(
                    first_name=str(form.cleaned_data.get('first_name')).upper(),
                     username = form.cleaned_data.get('username'),
                     password = form.cleaned_data.get('password1'),
                     last_name = str(form.cleaned_data.get('last_name')).upper(),
                     gstin_Number = form.cleaned_data.get('gstin_Number'),
                     businessid=busiID,
                     email = form.cleaned_data.get('email'),
                     is_active = True,
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
        
        return render(request, 'registration.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html", {})

@login_required
def subscribe(request):
    received_token = request.GET.get('token')
    stored_tokens = request.session.get('redirect_tokens', {})
    if received_token and stored_tokens.get(received_token):
        # Token is valid! Remove it so it can't be reused.
        del stored_tokens[received_token]
        request.session['redirect_tokens'] = stored_tokens
        request.session.save() # Save the updated session
        if request.method == 'POST':
            subid = subscriptionsid()
            subscription = subscriptions(subscriptionid = subid,
                                            businessid = User.objects.get(username= request.user).businessid,
                                            start_date = timezone.now(),
                                            end_date = datetime.timedelta(days=30)+timezone.now(),
                                            amount = 850,
                                            duration = datetime.timedelta(days=30),
                                            transaction_id = str(get_random_string(14).upper()),
                                            Discount = 0,
                                            payment_status = 'paid',
                                            is_valid = True)
            subid.save()
            subscription.save()
            current_user = User.objects.get(username=request.user)
            current_user.subscription = subscription.subscriptionid
            current_user.save()
            return redirect('sub_complete')
        return render(request, 'subscription/subscribe.html', {})
    else:
         # Deny direct access or access with invalid/missing token
        return Http404("Page not found or invalid access token.")
        # Or return HttpResponseBadRequest("Invalid or missing access token.")

def password_reset(request):
    return render(request, 'password_reset.html', {})

@login_required    
def sub_complete(request):
    return render(request, 'subscription/subscription_complete.html')

@login_required
def sub_history(request):
    if request.method == 'GET':
        data = list(subscriptions.objects.filter(businessid = User.objects.get(username=request.user).businessid).order_by('-subscriptionid').values())
        data_to_json = {'data':[]}
        for item in data:
            temp = {}
            for key in ['start_date', 'end_date', 'amount', 'duration', 'transaction_id']:
                temp[key] = str(item[key]).split(' ')[0]
            data_to_json['data'].append(temp)
        return render(request, 'subscription/subscription_history.html', {'data': json.dumps(data_to_json)})
    
@login_required
def sub_history_detail(request, sub_data):
    if request.method=='GET':
        return render(request, 'subscription/sub_history_detail.html', {'data': sub_data})
    else:
        return redirect('index')


def email_confirm(request):
    if request.method=='GET':
        return render(request, '')
    else:
        return redirect('login')