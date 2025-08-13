from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('legacy/', views.legacy, name='legacy'),
    path('services/', views.services, name='services'),
    path('dealership_service/', views.dealership, name='dealership'),
    path('store/', views.store, name='store'),
    path('future/', views.future, name='future'),
]