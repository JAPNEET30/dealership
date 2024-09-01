from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.current, name='current'),
    path('incoming/', views.incoming, name='incoming'),
    path('outgoing/', views.outgoing, name='outgoing'),
    path('damaged/', views.damaged, name='damaged'),
    path('search/', views.search, name='search'),
]

urlpatterns+=[
    # path('current/<str>', views.current, name='current_search'),
    # path('incoming/<str>', views.incoming, name='incoming_search'),
    # path('outgoing/<str>', views.outgoing, name='outgoing_search'),
    # path('damaged/<str>', views.damaged, name='damaged_search'),
    path('search/<str>', views.search, name='search'),
    ]