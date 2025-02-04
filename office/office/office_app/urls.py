from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create_office/' , create_office , name = 'create_office'),
    path('list_office/' , list_office , name = 'list_office'),
    path('delete_office/<int:record_id>/' , delete_office , name = 'delete_office')
]