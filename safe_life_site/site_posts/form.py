from django import forms
from .models import Posts, Images, Branches

class PostEdit(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title_image', 'title', 'main_text', 'text', 'file', 'branche']

class PostImageDawnlod(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']