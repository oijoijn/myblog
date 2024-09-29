from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    # 管理画面で表示されるフィールド
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # ユーザー作成時に表示されるフィールド
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    
    list_display = ('username', 'email', 'is_staff', 'is_active', 'is_superuser')  # 管理画面のユーザー一覧で表示されるフィールド
    search_fields = ('username', 'email')  # 検索可能なフィールド
    ordering = ('username',)  # 並び順

# CustomUser を管理画面に登録
admin.site.register(CustomUser, CustomUserAdmin)
