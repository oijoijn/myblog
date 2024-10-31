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
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'コメントを入力してください...'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ラベルを空に設定
        self.fields['comment'].label = ''
