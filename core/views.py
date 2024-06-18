from django.shortcuts import render
from books.models import Book
from categories.models import Category
# Create your views here.

def home(request,category_slug=None):
  books=Book.objects.all()
  categories=Category.objects.all()
  if category_slug is not None:
    category=Category.objects.get(slug=category_slug)
    books=Book.objects.filter(category=category)

  return render(request,'home.html',{'books':books,'categories':categories})