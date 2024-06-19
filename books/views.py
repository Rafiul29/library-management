from django.shortcuts import render,redirect
from . import models
from django.views.generic import DetailView
from . import forms
from . import models
# Create your views here.

class DetailBookView(DetailView):
  model=models.Book
  pk_url_kwarg='id'
  template_name='book_details.html'

  def post(self, request, *args, **kwargs):
      review_form = forms.ReviewForm(data=self.request.POST)
      book = self.get_object()
      if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.user=request.user
            new_review.book = book
            new_review.save()
      return self.get(request, *args, **kwargs)

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    book=self.object
    reviews=book.reviews.all()
    reviews_form=forms.ReviewForm()
    context['reviews']=reviews
    context['reviews_form']=reviews_form
    return context
