from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from usercore.models import subscriptions
# from django.utils import timezone
from .models import *
from .forms import excel_data_entry

#functions
def fetch_for_dashboard(busiID):
    locations_list = list(locations.objects.filter(businessID=busiID).values('name','tag'))
    return locations_list

#views
@login_required
def write_data(request):
    form = excel_data_entry()
    user = request.user
    # if user.admin_access:
    #     data={'form':'form'}

    # elif user.insurance_add_access:
    #     pass

    # elif user.stock_add_access:
    #     pass

    # elif user.workshop_add_access:
    #     pass

    # else:
    #     JsonResponse({'data':'Unauthorized access requested.'})
    return render(request, 'data_ops/add_data.html', context={'form':form})

@login_required
def get_data(request, site):
    return render(request, '')

@login_required
def update_data(request, site):
    return render(request, '')

@login_required
def delete_data(request, site):
    return render(request, '')

@login_required
def get_user(request):
    return JsonResponse({
        'user':str(request.user.first_name+' '+request.user.last_name).capitalize()
    })

@login_required
def get_subscription(request):
    busiID = request.user.businessid
    subscription = subscriptions.objects.filter(businessid=busiID).order_by('subscriptionid').values('end_date')
    # if list(subscription)[0]['end_date']<timezone.now():
    #     print('sub ended')
    # else:
    #     print('valid')
    return JsonResponse({
        'subscription':str(subscription)#[0]['end_date']
    })

@login_required
def get_dashboard(request):
    busiID = request.user.businessid
    data=fetch_for_dashboard(busiID)
    return JsonResponse(data={
        'vehicle_data':data
    })