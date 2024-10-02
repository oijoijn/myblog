from django.urls import path  # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="index"),
    path("article/<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)