from django.urls import path 

from .views import *

urlpatterns = [
    path('message_list/' , message_list , name = 'message_list'),
    path('message_create/' , message_create , name = 'message_create'),
    path('message_details/<int:contact_id>/' , message_details , name = 'message_details'),
    path('message_delete/<int:contact_id>/' , message_delete , name = 'message_delete')
]