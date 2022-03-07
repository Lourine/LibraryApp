from django import forms
from .models import Book

#Forms
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'