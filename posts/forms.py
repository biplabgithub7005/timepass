
from django import forms
from .models import Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image','title')

    title= forms.CharField(
        widget=forms.Textarea(

        )
    )