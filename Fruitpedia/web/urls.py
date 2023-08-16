from django.urls import path
from .views import (
    index_view,
    dashboard_view,
    fruit_create_view,
    fruit_details_view,
    fruit_edit_view,
    fruit_delete_view,
    profile_create_view,
    profile_details_view,
    profile_edit_view,
    profile_delete_view,
)

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create/', fruit_create_view, name='fruit_create'),
    path('<int:fruit_id>/details/', fruit_details_view, name='fruit_details'),
    path('<int:fruit_id>/edit/', fruit_edit_view, name='fruit_edit'),
    path('<int:fruit_id>/delete/', fruit_delete_view, name='fruit_delete'),
    path('profile/create/', profile_create_view, name='profile_create'),
    path('profile/details/', profile_details_view, name='profile_details'),
    path('profile/edit/', profile_edit_view, name='profile_edit'),
    path('profile/delete/', profile_delete_view, name='profile_delete'),

]