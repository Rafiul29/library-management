from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(forms.ModelForm):
  def __init__(self,*args, **kwargs):
        super(ModelForm,self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class':'shadow-sm bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full px-5 py-2  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light'})
  
  class Meta:
    model=Review
    fields=['text','rating']

  
