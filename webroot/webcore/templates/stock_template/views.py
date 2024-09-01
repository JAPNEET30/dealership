from anaconda_cloud_auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import render

@login_required
@never_cache
def search(request):
    return(render(request, 'stock_template/search_stock.html'))
@login_required
@never_cache
def current(request):
    user = request.user
    businessid = user.businessid
    data = [{'Model':'Activa','Varient':'Drum', 'Location':'Hq1','Quantity':'10'},
            {'Model':'Splender','Varient':'Disc', 'Location':'Hq1','Quantity':'20'},]
    return(render(request, 'stock_template/current_stock.html', context={'table_title':'Current Standings','table_headers':['Model','Varient','Location','Quantity'],'data_table':data}))

@login_required
@never_cache
def incoming(request):
    data=[
          ]
    
    return(render(request, 'stock_template/incoming_stock.html', context={'data_table':data}))

@login_required
@never_cache
def outgoing(request):
    data=[
          ]
    return(render(request, 'stock_template/outgoing_stock.html', context={'data_table':data}))

@login_required
@never_cache
def damaged(request):
    data=[{}

    ]
    return(render(request, 'stock_template/damaged_stock.html', context={'data_table':data}))

@login_required
@never_cache
def extras(request):
    data=[{'BatteryNo':'oih49f943hf90y','Date_of Manufacturing':'3/2023','In_stock_from':'19/03/2024'}]
    return(render(request, 'stock_template/extras_stock.html', context={'data_table':data}))

@login_required
@never_cache
def missing(request):
    data=[{'Reported_by':'Rakesh','content':'1 vehicle', 'SerialNo':'iy32r9823yr0'}]
    return(render(request, 'stock_template/missing_stock.html', context={'data_table':data}))