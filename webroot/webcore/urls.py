from django.urls import path, include

from . import ajax_urls
from . import views
from .templates.stock_template import urls as stock_urls
from .templates.track_template import urls as track_urls
from .templates.teams_template import urls as teams_urls

urlpatterns =[
    path('', views.index, name='index'),
    path('stock/', views.stock, name='stock'),
    path('workshop/', views.workshop, name='workshop'),
    path('service/', views.service, name='service'),
    path('insurance/', views.insurance, name='insurance'),
    # path('department/', views.department, name='department'),
    path('subscription/', views.subscription, name='subscription'),
]

urlpatterns+=[
    path('data/', include(ajax_urls)),
    path('stock_view/', include(stock_urls)),
    path('track/', include(track_urls)),
    path('teams/', include(teams_urls)),
]