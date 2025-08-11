from django.urls import path, include
from . import views

urlpatterns =[
    path('', views.teams, name='teams'),
    path('new_team/', views.new_team, name='new_team'),
    path('new_member/', views.new_member, name='new_member'),
    path('manage_teams/', views.manage_teams, name='manage_teams'),
    path('manage_members/', views.manage_members, name='manage_members'),
    path('manage_attendance/', views.manage_attendance, name='manage_attendance'),
    path('member_template/', views.member_template, name='members_template'),
    path('team_template/', views.team_template, name='team_template'),
]

urlpatterns+=[
    path('adding_member/', views.adding_member, name='adding_member'),
]