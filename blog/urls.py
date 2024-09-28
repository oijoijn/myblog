from django.urls import path, include
from . import views

urlpatterns = [
    path('self_introduction/', views.index),
]
