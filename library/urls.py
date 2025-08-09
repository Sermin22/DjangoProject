from django.urls import path
from library.apps import LibraryConfig
# from . import views
from .views import (BooksListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
                    AuthorCreateView, AuthorUpdateView, AuthorListView, AuthorDetailView, AuthorDeleteView,
                    RecommendBookView, ReviewBookView)

app_name = LibraryConfig.name

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/new/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/<int:pk>/recommend/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/<int:pk>/review/', ReviewBookView.as_view(), name='book_review'),


    # path('books_list/', views.books_list, name='books_list'),
    # path('book_detail/<int:book_id>/', views.book_detail, name='book_detail'),
]
