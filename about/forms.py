from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    # post = forms.IntegerField(widget=forms.HiddenInput)  # Add a hidden post field

    class Meta:
        model = Comment
        fields = ('post', 'body',)