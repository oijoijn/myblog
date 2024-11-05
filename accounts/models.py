from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    アカウントを作成する際の設定
    """
    def create_user(self, username, password=None, email=None, **extra_fields):
        """
        動作: ユーザの新規追加で使用
        """
        if not username:
            raise ValueError('ユーザ名を入力してください')

        if email:
            email = self.normalize_email(email)

        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, email=None, **extra_fields):
        """
        動作: superuserの新規追加で使用
        """
        # superuser 作成時には email が必須
        if not email:
            raise ValueError('Superuser にはメールアドレスが必要です')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username=username, password=password, email=email, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    アカウントを作成するfield
    USERNAME_FIELD ログイン時にusernameとpassword(自動使用)を使用
    """
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # emailを必須フィールドとして追加

    objects = CustomUserManager()

    def __str__(self):
        return self.username

