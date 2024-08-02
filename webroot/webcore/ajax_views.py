from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from usercore.models import subscriptions
# from django.utils import timezone
from .models import *
from .forms import *
from pandas import read_excel

#functions
def fetch_for_dashboard(busiID):
    locations_list = list(locations.objects.filter(businessID=busiID).values('name','tag'))
    return locations_list

#views
@login_required
def write_data(request):
    excel_form = vehicle_excel_entry()
    manual_form = vehicle_manual_entry()
    user = request.user
    busiID= user.businessid
    manual_form.model_name.choices([[choice],[str(choice).replace(' ','')]] for choice in list(categories.object.filter(businessid=busiID).values()))
    return render(request, 'data_ops/add_data.html', {'excel_form':excel_form,'manual_form':manual_form})

@login_required
def get_data(request):
    return render(request, '')

@login_required
def update_data(request):
    return render(request, '')

@login_required
def delete_data(request):
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

@login_required
def get_catandloc(request):
    context = {'cat_manual_form':category_manual_entry,
               'cat_excel_form':category_upload_entry,
               'loc_manual_form':location_manual_entry}
    return render(request, 'data_ops/add_categories.html', context)

@login_required
def get_cat_manual(request):
    user = request.user
    busiID = user.businessid
    if request.method == 'POST':
        form = category_manual_entry(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Success'}, status=200)
        elif 'is_accessories_included' not in form.cleaned_data and 'model_name'and 'colors' and 'varients' in form.cleaned_data:
            form.cleaned_data['is_accessories_included'] = False
            form.cleaned_data['accessories_listed'] = ''
            if form.is_valid:
                print(form.cleaned_data)
                return JsonResponse(data={'data':'Success'}, status=200)
            else:
                print(form.cleaned_data)
                return JsonResponse(data={'data':'Error'}, status=400)    
        else :
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Error'}, status=400)

@login_required
def get_cat_excel(request):
    if request.method == 'POST':
        form = category_upload_entry(request.POST, request.FILES)
        if form.is_valid():
            file = read_excel(request.FILES.get('cat_file'))
            print(file.values.tolist())
            return JsonResponse(data={'data':'Success'}, status=200)
        else:
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Success'}, status=400)

@login_required
def get_loc_manual(request):
    user = request.user
    busiID = user.businessid
    if request.method == 'POST':
        form = category_manual_entry(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Success'}, status=200)
        elif 'is_accessories_included' not in form.cleaned_data and 'model_name'and 'colors' and 'varients' in form.cleaned_data:
            form.cleaned_data['is_accessories_included'] = False
            form.cleaned_data['accessories_listed'] = ''
            if form.is_valid:
                print(form.cleaned_data)
                return JsonResponse(data={'data':'Success'}, status=200)
            else:
                print(form.cleaned_data)
                return JsonResponse(data={'data':'Error'}, status=400)    
        else :
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Error'}, status=400)