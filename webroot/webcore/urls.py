from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('stock/', views.stock, name='stock'),
    path('workshop/', views.workshop, name='workshop'),
    path('service/', views.service, name='service'),
    path('insurance/', views.insurance, name='insurance'),
    path('department/', views.department, name='department')
]