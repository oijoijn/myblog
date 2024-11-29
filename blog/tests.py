from django.test import TestCase
from django.urls import reverse
from .models import BlogPost, Comment
from django.contrib.auth import get_user_model

User = get_user_model()

class BlogPostModelTest(TestCase):
    def test_blog_post_creation(self):
        post = BlogPost.objects.create(
            title="Test Post", html_file="blog/article.html", img_file="images/test.png"
        )
        self.assertEqual(post.title, "Test Post")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = BlogPost.objects.create(title="Test Post", html_file="blog/article.html", img_file="images/test.png")

    def test_comment_creation(self):
        comment = Comment.objects.create(post=self.post, user=self.user, comment="Test Comment")
        self.assertEqual(comment.comment, "Test Comment")
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.user, self.user)

class BlogPostListViewTest(TestCase):
    def setUp(self):
        self.post = BlogPost.objects.create(title="Test Post", html_file="blog/article.html", img_file="images/test.png")

    def test_blog_post_list_view(self):
        response = self.client.get(reverse("blog:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

class BlogPostDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = BlogPost.objects.create(title="Test Post", html_file="blog/article.html", img_file="images/test.png")

    def test_blog_post_detail_view(self):
        response = self.client.get(reverse("blog:article_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

class EditCommentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = BlogPost.objects.create(title="Test Post", html_file="blog/article.html", img_file="images/test.png")
        self.comment = Comment.objects.create(post=self.post, user=self.user, comment="Original Comment")

    def test_edit_comment_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("blog:edit_comment", kwargs={"pk": self.comment.pk}),
            {"comment": "Updated Comment"},
        )
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.comment, "Updated Comment")

