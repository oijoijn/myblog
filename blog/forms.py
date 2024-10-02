from django import forms
from . import models

class CommentForm(forms.ModelForm):
    """
    動作:formの作成
    """
    class Meta:
        model = models.Comment
        fields = ["comment"]
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'コメントを入力してください...'}),
        }
