from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist
from . import models, forms

class BlogPostListView(ListView):
    """
    動作:記事を表示する
    """
    model = models.BlogPost
    template_name = 'index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

@method_decorator(login_required, name='dispatch')
class BlogPostDetailView(View):
    """
    動作:記事詳細ビュー & コメント投稿 (DetailView + View)
    クラスベースビューにログインを要求する
    """

    def get(self, request, pk):
        article = get_object_or_404(models.BlogPost, pk=pk)
        comments = article.comments.all()
        form = forms.CommentForm()

        # pkに基づいてテンプレート名を動的に決定
        template_name = article.html_file

        # テンプレートが存在しない場合に404を返すためのチェック
        dict = {
                'article': article, 
                'comments': comments, 
                'form': form
            }
        try:
            return render(request, template_name, dict)
        except TemplateDoesNotExist:
            raise Http404("Template not found")

    def post(self, request, pk):
        article = get_object_or_404(models.BlogPost, pk=pk)
        comments = article.comments.all()
        form = forms.CommentForm(request.POST)
        
        # ログインユーザーのみコメント可能にする
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = article  # 修正箇所
                comment.user = request.user  # ログインユーザーを自動的に取得
                comment.save()
                return redirect('blog:article_detail', pk=article.pk) 
        
        # pkに基づいてテンプレート名を動的に決定
        template_name = f'blog/docker_tutorial_{pk}.html'
        dict = {
            'article': article,
            'comments': comments,
            'form': form
        }

        return render(request, template_name, dict)

    # Commentモデルの__str__メソッド
    def __str__(self):
        return f"Comment by {self.user} on {self.post}"
