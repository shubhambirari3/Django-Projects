from django.urls import path 

from .views import *

urlpatterns = [
    path('task_list/' , task_list , name='task_list'),
    path('task_create/' , task_create , name='task_create'), # this name is used in the html file to create  dynamicallly  to redirect to the task_create page like this {% url 'task_create' %}
    path('task_update/<int:task_id>/' , task_update , name='task_update'),
    path('task_delete/<int:task_id>/' , task_delete , name='task_delete'),  # Add this line
    path('task_toggle_complete/<int:task_id>/' , task_toggle_complete , name='task_toggle_complete'),  # Add this line
]