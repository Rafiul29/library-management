from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:id>/',views.DetailBookView.as_view(),name='book_details'),
    path('borrow/<int:id>/', views.borrow_book, name='borrow_book'),
    path('borrows/', views.all_borrow_book, name='all_borrow_book'),
    path('return_book/<int:id>', views.return_book, name='return_book'),
]


