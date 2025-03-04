
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('create_items/', create_items, name='create_items'),
    path('list_items/', list_items, name='list_items'),
    path('update_items/<int:id>/', update_items, name='update_items'),
    path('delete_items/<int:id>/', delete_items, name='delete_items'),
    path('login/', login_page, name='login_page'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', logout_user, name='logout_user'),
]  
