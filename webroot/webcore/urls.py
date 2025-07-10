from django.urls import path, include

from . import ajax_urls
from . import views
from .templates.stock_template import urls as stock_urls

urlpatterns =[
    path('', views.index, name='index'),
    path('stock/', views.stock, name='stock'),
    path('track/', views.track, name='track'),
    path('workshop/', views.workshop, name='workshop'),
    path('service/', views.service, name='service'),
    path('insurance/', views.insurance, name='insurance'),
    path('department/', views.department, name='department'),
    path('subscription/', views.subscription, name='subscription'),
]

urlpatterns+=[
    path('data/', include(ajax_urls)),
    path('stock_view/', include(stock_urls)),
]