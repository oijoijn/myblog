from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # 追加
from .import models


class SignUpForm(UserCreationForm):
    """
    動作:signupform
    usernameフィールドのラベルを変更
    """
    class Meta:
        model = models.CustomUser
        fields = ["username"]
        labels = {"username": "ニックネーム"}

# ログインフォームを追加
class LoginForm(AuthenticationForm):
    """
    動作:LoginForm
    usernameフィールドのラベルを変更
    """
    class Meta:
        model = models.CustomUser

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "ニックネーム"