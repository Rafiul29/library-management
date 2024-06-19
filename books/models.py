from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from books.constrants import RATING_CHOISE

# Create your models here.
class Book(models.Model):
  title=models.CharField(max_length=100)
  description=models.TextField()
  image=models.ImageField(upload_to='books/images',default='books/images/default.png')
  borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
  category=models.ManyToManyField(Category,related_name='books')
    
  def __str__(self) -> str:
    return self.title
  
class Borrow(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  book=models.ForeignKey(Book,on_delete=models.CASCADE)
  borrowing_date=models.DateTimeField(auto_now_add=True)
  returned=models.BooleanField(default=False)

  def __str__(self) -> str:
    return self.user.first_name

class Review(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')
  book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')
  text=models.CharField(max_length=30)
  created_on=models.DateTimeField(auto_now_add=True)
  rating = models.CharField(max_length=50,choices=RATING_CHOISE)

  def __str__(self) -> str:
    return f'review by {self.user.first_name}'