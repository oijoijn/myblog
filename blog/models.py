from django.db import models
from django.conf import settings
from django.utils import timezone

class Article(models.Model):
    """
    動作:記事のモデル
    """
    title = models.CharField(max_length=100)
    content = models.TextField()  # 管理者がHTMLで記事を書く
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    pdf_file = models.FileField(upload_to='pdfs/', blank=True, null=True)
    image_file = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"title: {self.title}, owner: {self.owner.username}"

class Comment(models.Model):
    """
    動作:コメント
    """
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.user} on {self.article}"