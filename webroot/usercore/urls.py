from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
from django.views.generic import RedirectView
 
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('email/confirm', views.email_confirm, name='email_confirm'),
    path('register/', views.register, name='register'),
    path('subscribe/', views.subscribe, name='subscription'),
    path('sub_complete', views.sub_complete, name='sub_complete'),
    path('sub_history', views.sub_history, name='sub_history'),
    path('sub_history/<str:sub_data>', views.sub_history_detail, name='sub_history_detail'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
]
