from django.urls import path  # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogPostListView.as_view(), name="index"),
    path("article/<int:pk>/", views.BlogPostDetailView.as_view(), name="article_detail"),
    path('comment/edit/<int:pk>/', views.EditCommentView.as_view(), name='edit_comment'),
]
