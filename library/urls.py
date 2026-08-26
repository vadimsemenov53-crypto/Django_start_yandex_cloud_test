from django.urls import path
from library.apps import LibraryConfig
# from library.views import book_list, book_detail

from library.views import (BookListView, BookCreateView, BookDeleteView, BookDetailView, BookUpdateView,
                           AuthorCreateView, AuthorUpdateView, AuthorListView, RecommendBookView, ReviewBookView)

app_name = LibraryConfig.name

urlpatterns = [
    # path('book_list/', book_list, name='book_list'),
    # path('book_detail/<int:book_id>', book_detail, name='book_detail'),

    path('books/', BookListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),

    path('author/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),

    path('books/recomend/<int:pk>/', RecommendBookView.as_view(), name='book_recomend'),
    path('books/review/<int:pk>/', ReviewBookView.as_view(), name='book_review'),
]
