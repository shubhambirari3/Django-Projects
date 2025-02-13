from django.urls import path
from .views import *

urlpatterns = [
    path('task_list/', task_list, name='task_list'),
    path('task_create/', task_create, name='task_create'),
    path('task_update/<slug:slug>/', task_update, name='task_update'),
    path('task_delete/<slug:slug>/', task_delete, name='task_delete'),
    path('task_toggle_complete/<slug:slug>/', task_toggle_complete, name='task_toggle_complete'),
]