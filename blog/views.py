from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, UpdateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models, forms

class BlogPostListView(LoginRequiredMixin, ListView):
    """
    動作:記事を表示する
    """
    model = models.BlogPost
    template_name = 'index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context

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

class EditCommentView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''
    動作:コメントの編集
    loginuserしかできない
    '''
    model = models.Comment
    form_class = forms.CommentForm
    template_name = 'blog/edit_comment.html'
    context_object_name = 'comment'

    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.post.pk})

    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user
