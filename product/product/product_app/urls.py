from django.contrib import admin 
from django.urls import path 
from .views import *

urlpatterns = [
    path('product_list/' , product_list , name="product_list"),
    path('product_create/' , product_create , name="product_create"),
    path('product_update/<int:product_id>/', product_update , name="product_update"),
    path('product_delete/<int:product_id>/' , product_delete , name = "product_delete" )

]