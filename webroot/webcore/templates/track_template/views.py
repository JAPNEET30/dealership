from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_GET, require_http_methods, require_POST, require_safe
from django.shortcuts import render

@login_required
def track(request):
    return(render(request, 'track_template/track.html'))

@login_required
def package_view(request, number):
    return(render(request, 'track_template/package_view.html', {'number': number}))


@login_required
@never_cache
def new_package(request):
    return(render(request, 'track_template/new_package.html'))


@login_required
@never_cache
def package_history(request):
    return(render(request, 'track_template/package_history.html'))


@login_required
@never_cache
def package_template(request):
    return(render(request, 'track_template/package_template.html'))

@login_required
@never_cache
def network(request):
    return(render(request, 'track_template/package_network.html'))

def network_accounts(request):
    return(render(request, 'track_template/package_network.html'))


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