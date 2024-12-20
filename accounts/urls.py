from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('user/comments/', views.UserCommentsView.as_view(), name='user_comments'),
    path('update/', views.ChangePasswordView.as_view(), name='user_update'),
]

