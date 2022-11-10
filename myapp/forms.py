from django import forms

from .models import Posst

class PostForm(forms.ModelForm):

    class Meta:
        model = Posst
        fields = ('title', 'text',)