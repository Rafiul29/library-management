from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('details/<int:id>/',views.DetailBookView.as_view(),name='book_details'),
]


