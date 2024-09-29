from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from . import forms

class IndexView(TemplateView):
    """
    動作:home
    """
    template_name = "index.html"


class SignupView(CreateView):
    """
    動作:ユーザー登録
    """
    form_class = forms.SignUpForm 
    template_name = "accounts/signup.html" 
    success_url = reverse_lazy("accounts:index") 

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
    success_url = reverse_lazy("accounts:index")