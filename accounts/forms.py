from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, ReadOnlyPasswordHashField
from .import models
from django import forms

class SignUpForm(UserCreationForm):
    """
    動作:signupform
    usernameフィールドのラベルを変更
    """
    class Meta:
        model = models.CustomUser
        fields = ["username", "password1", "password2"]  # パスワードフィールドも追加
        labels = {"username": "", "password1": "", "password2": ""}  # ラベルを削除

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # ラベルを空に設定
        self.fields['username'].label = ""  # ニックネームのラベルを削除
        self.fields['password1'].label = ""  # パスワードのラベルを削除
        self.fields['password2'].label = ""  # パスワード確認のラベルを削除

        # placeholderを追加
        self.fields['username'].widget.attrs['placeholder'] = 'ニックネームを入力してください'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワードを入力してください'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワードを再入力してください'  # パスワード確認フィールドにplaceholderを追加



class LoginForm(AuthenticationForm):
    """
    動作:LoginForm
    usernameフィールドのラベルを変更
    """
    class Meta:
        model = models.CustomUser
        fields = ["username", "password"]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        # ラベルを空に設定
        self.fields['username'].label = ""  # ニックネームのラベルを削除
        self.fields['password'].label = ""  # パスワードのラベルを削除

        # placeholderを追加
        self.fields['username'].widget.attrs['placeholder'] = 'ニックネームを入力してください'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワードを入力してください'  # パスワードフィールドにplaceholderを追加


class ChangePassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())