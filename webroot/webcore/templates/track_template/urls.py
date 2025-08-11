from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.track, name='track'),
    path('new_package/', views.new_package, name='new_package'),
    path('package_history/', views.package_history, name='package_history'),
    path('package_/', views.package_template, name='package_'),
    path('package_history/<int:number>/', views.package_view, name='package_view'),
    path('network/', views.network, name='network'),
    path('network_accounts/', views.network_accounts, name='network_accounts'),
]