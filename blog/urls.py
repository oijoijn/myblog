from django.urls import path 
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("self_introduction/", views.self_introduction, name="self_introduction"),
]
