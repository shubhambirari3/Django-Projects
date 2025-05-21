from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
    path('create_items/', create_items, name='create_items'),
    path('home/', list_items, name='list_items'),
    path('update_items/<int:id>/', update_items, name='update_items'),
    path('delete_items/<int:id>/', delete_items, name='delete_items'),
    path('login/', login_page, name='login_page'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', logout_user, name='logout_user'),
    path('toggle_checked/<int:id>/', views.toggle_checked, name='toggle_checked'),
]
