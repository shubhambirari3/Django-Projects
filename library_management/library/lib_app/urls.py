from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/update/<int:id>/', views.book_update, name='book_update'),
    path('books/delete/<int:id>/', views.book_delete, name='book_delete'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.author_create, name='author_create'),
    path('authors/update/<int:id>/', views.author_update, name='author_update'),
]