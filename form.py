from django import forms
from board.models import Boards,Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'content',}
