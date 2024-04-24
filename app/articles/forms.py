from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', 'parent']
        widgets = {
            'message': forms.TextInput(attrs={
                'id': 'name',
                'class': 'form-control'
            }),
        }
