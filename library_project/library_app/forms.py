from library_app.models import *
from django import forms

class ModelAuthor(forms.ModelForm):

    class Meta:
        model=Author
        exclude='__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class ModelBook(forms.ModelForm):

    class Meta:
        model=Book
        fields='__all__'

class ModelGenre(forms.ModelForm):

    class Meta:
        model=Genre
        fields='__all__'