from django.urls import path
from flask import redirect
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
]