from django.urls import path
from library.apps import LibraryConfig
from . import views
from .views import BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView



app_name = LibraryConfig.name

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),
    # path('books_list/', views.books_list, name='books_list'),
    # path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]