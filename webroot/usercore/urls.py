from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.views.generic import RedirectView
 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('subscribe/', views.subscribe, name='subscription'),
    path('', RedirectView.as_view(pattern_name='login', permanent=False))
    # path('admin/', admin.site.urls),
]