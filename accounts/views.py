from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Comment
from . import forms, models

class SignupView(CreateView):
    """
    動作:ユーザー登録
    """
    form_class = forms.SignUpForm 
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("blog:index") 

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response


class LoginView(LoginView):
    """
    動作:login
    """
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class LogoutView(LogoutView):
    """
    動作:logout
    """
    success_url = reverse_lazy("blog:index")

class UserCommentsView(LoginRequiredMixin, ListView):
    '''
    動作:コメントの取得
    loginuserしかできない
    '''
    model = Comment
    template_name = 'accounts/user_comments.html'
    context_object_name = 'comments'

    # ログインユーザーのコメントのみを取得
    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('blog:index')
    template_name = 'accounts/user_update.html'
