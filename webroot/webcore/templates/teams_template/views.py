from anaconda_cloud_auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET, require_http_methods, require_POST, require_safe
from django.shortcuts import render

@login_required
def teams(request):
    return(render(request, 'teams_template/teams.html'))

@login_required
@never_cache
def new_team(request):
    return(render(request, 'teams_template/new_team.html'))


@login_required
@never_cache
def new_member(request):
    return(render(request, 'teams_template/new_member.html'))


@login_required
@never_cache
def member_template(request):
    return(render(request, 'teams_template/member_template.html'))

@login_required
@never_cache
def team_template(request):
    return(render(request, 'teams_template/team_template.html'))

@login_required
@never_cache
def manage_teams(request):
    return(render(request, 'teams_template/manage_teams.html'))

@login_required
@never_cache
def manage_members(request):
    return(render(request, 'teams_template/manage_members.html'))

@login_required
@never_cache
def manage_attendance(request):
    return(render(request, 'teams_template/manage_attendance.html'))

##API views from here

@login_required
@never_cache
def get_package_number(request):
    return render(request,'')

@login_required
@never_cache
@require_POST
def store_package(request):
    return render(request, '')