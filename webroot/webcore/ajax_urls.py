from django.urls import path
from . import ajax_views

urlpatterns = [
    path('create/', ajax_views.write_data, name='write_data'),
    path('update/', ajax_views.update_data, name='update_data'),
    path('delete/', ajax_views.delete_data, name='delete_data'),
    path('read/', ajax_views.get_data, name='read_data'),
    path('get_user/', ajax_views.get_user, name='get_user'),
    path('get_sub/', ajax_views.get_subscription, name='get_sub'),
    path('get_catandloc/', ajax_views.get_catandloc, name='get_catandloc'),
    path('category_data/manual/', ajax_views.get_cat_manual, name='get_cat_manual'),
    path('category_data/auto/', ajax_views.get_cat_excel, name='get_cat_excel'),
    path('location_data/manual/', ajax_views.get_loc_manual, name='get_loc_manual'),
]