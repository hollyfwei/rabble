"""
for creating a PostForm form for creating/editing posts
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }
        labels = {
            'title': 'Title',
            'body': 'Body'
        }