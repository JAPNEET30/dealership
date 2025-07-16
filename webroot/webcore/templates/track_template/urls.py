from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.track, name='track'),
    path('new_package/', views.new_package, name='new_package'),
    path('package_history/', views.package_history, name='package_history'),
    path('package_/', views.package_template, name='package_'),
    
]