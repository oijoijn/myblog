from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, UpdateView
from django.views import View
from django.http import Http404
from django.template.exceptions import TemplateDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models, forms

class BlogPostListView(ListView):
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

class BlogPostDetailView(View):
    """
    動作:記事詳細ビュー & コメント投稿 (DetailView + View)
    postはログインユーザー限定
    """
    def dispatch(self, request, *args, **kwargs):
        # POSTリクエストのみ認証チェック
        if request.method == "POST" and not request.user.is_authenticated:
            return redirect('accounts:login')  # ログインページにリダイレクト
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        article = get_object_or_404(models.BlogPost, pk=pk)
        comments = article.comments.all()
        form = forms.CommentForm()

        # pkに基づいてテンプレート名を動的に決定
        template_name = article.html_file
        print(template_name)

        # テンプレートが存在しない場合に404を返すためのチェック
        dict = {
                'article' : article,
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
        # pkに基づいてテンプレート名を動的に決定
        template_name = article.html_file

        dict = {
            'article' : article,
            'comments': comments,
            'form': form
        }

        # ログインユーザーのみコメント可能にする
        if request.user.is_authenticated:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = article  # 修正箇所
                comment.user = request.user  # ログインユーザーを自動的に取得
                comment.save()
                return  redirect('blog:article_detail', pk=article.pk)

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

    #ture or false を返す, loginuserで自分子コメントしか編集できない
    def test_func(self):
        comment = self.get_object()
        return comment.user == self.request.user
