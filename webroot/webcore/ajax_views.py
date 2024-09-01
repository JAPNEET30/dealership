from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from usercore.models import subscriptions
# from django.utils import timezone
from .models import *
from .forms import *
from pandas import read_excel
from django.db import transaction

#functions
@login_required
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
            with transaction.atomic():
                    cat = categories.objects.create(businessid=busiID,
                                              model_name=form.cleaned_data['model_name'],
                                              other={'varients':form.cleaned_data['varients'],
                                                     'colors':form.cleaned_data['colors']},
                                                is_accessories_included = form.cleaned_data['is_accessories_included'],
                                                accessories=form.cleaned_data['accessories_listed'])
                    cat.save()
            return JsonResponse(data={'data':'Success'}, status=200)
        elif 'is_accessories_included' not in form.cleaned_data and 'model_name'and 'colors' and 'varients' in form.cleaned_data:
            form.cleaned_data['is_accessories_included'] = False
            form.cleaned_data['accessories_listed'] = ''
            if form.is_valid:
                print(form.cleaned_data)
                with transaction.atomic():
                    cat = categories.objects.create(businessid=busiID,
                                              model_name=form.cleaned_data['model_name'],
                                              other={'varients':form.cleaned_data['varients'],
                                                     'colors':form.cleaned_data['colors']},
                                                is_accessories_included = form.cleaned_data['is_accessories_included'],
                                                accessories=form.cleaned_data['accessories_listed'])
                    cat.save()
                return JsonResponse(data={'data':'Success'}, status=200)
            else:
                print(form.cleaned_data)
                return JsonResponse(data={'errors':'Error'}, status=400)    
        else :
            print(form.cleaned_data)
            return JsonResponse(data={'errors':'Error'}, status=400)

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
            return JsonResponse(data={'error':form.errors}, status=400)

@login_required
def get_loc_manual(request):
    user = request.user
    busiID = user.businessid
    if request.method == 'POST':
        form = location_manual_entry(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return JsonResponse(data={'data':'Success'}, status=200)
        elif 'tag' not in form.cleaned_data and 'name'and 'address' and 'type' in form.cleaned_data:
            form.cleaned_data['tag']=''
            if form.is_valid:
                print(form.cleaned_data)
                return JsonResponse(data={'data':'Success'}, status=200)
            else:
                print(form.cleaned_data)
                return JsonResponse(data={'errors':'Error'}, status=400)    
        else :
            print(form.cleaned_data)
            print(form.errors.as_data()['name'])
            return JsonResponse(data={"errors":form.errors.as_json()},status=400)

            
        
@login_required
def put_loc_table(request):
    user=request.user
    busiID = user.businessid
    locations_var = list(locations.objects.filter(businessid=busiID).values())

    if request.method=='GET':
        return JsonResponse({'locations':locations_var})
    
def put_cat_table(request):
    user=request.user
    busiID = user.businessid
    categories_var = list(categories.objects.filter(businessid=busiID).values())
    temp_model_name = [model['model_name'] for model in categories_var]
    temp_varients = [varient['other']['varients'] for varient in categories_var]
    temp_colors = [color['other']['colors'] for color in categories_var]
    temp_accessories = [accessory['accessories'] for accessory in categories_var]
    if request.method=='GET':
        return JsonResponse({'model_names':temp_model_name,
                             'varients':temp_varients,
                             'colors':temp_colors,
                             'accessories':temp_accessories})