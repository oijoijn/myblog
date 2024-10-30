from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    """
    動作:ブログ記事のメタデータを保存するモデル
    """
    title = models.CharField(max_length=255)  # 記事のタイトル
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_at = models.DateTimeField(auto_now=True)  # 更新日
    html_file = models.CharField(max_length=255)  # 記事に対応するHTMLファイルのパス

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    動作:コメント
    """
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_at = models.DateTimeField(auto_now=True)  # 更新日

    def __str__(self):
        return f"Comment by {self.user} on {self.article}"