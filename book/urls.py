from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_books, name="books"),
    path('add', views.add_book, name="add_book"),
    path('single/<int:book_id>', views.single_book, name='single_book'),
    path('add_comment/<int:book_id>', views.add_book_comment, name='add_comment')
]