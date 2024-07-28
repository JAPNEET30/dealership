from django.urls import path, include

from . import ajax_urls
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('stock/', views.stock, name='stock'),
    # path('stock/add', views.stockadd, name='add'),
    path('workshop/', views.workshop, name='workshop'),
    path('service/', views.service, name='service'),
    path('insurance/', views.insurance, name='insurance'),
    path('department/', views.department, name='department'),
    path('data/', include(ajax_urls)),
]