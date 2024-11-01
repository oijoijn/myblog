import os
import environ
from pathlib import Path
import django
from django.conf import settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")

# Static files settings
STATIC_DIR = Path.joinpath(BASE_DIR, env("STATIC_DIR"))
STATIC_URL = env('STATIC_URL')
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    STATIC_DIR,
]

print(f'STATIC_DIR: {STATIC_DIR}')
print(f'STATIC_URL: {STATIC_URL}')
print(f'STATIC_ROOT: {STATIC_ROOT}')

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('NAME'),  # データベース名
        'USER': env('USER_env'),  # ユーザー名
        'PASSWORD': env('PASSWORD'),  # パスワード
        'HOST': env('HOST'),  # ホスト名
        'PORT': env('PORT'),  # MySQLのデフォルトポート
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",  # オプション設定
        },
    }
}

print("Database Settings:")
print(f"ENGINE: {DATABASES['default']['ENGINE']}")
print(f"NAME: {DATABASES['default']['NAME']}")
print(f"USER: {DATABASES['default']['USER']}")
print(f"PASSWORD: {DATABASES['default']['PASSWORD']}")  # パスワードを表示
print(f"HOST: {DATABASES['default']['HOST']}")
print(f"PORT: {DATABASES['default']['PORT']}")
print(f"OPTIONS: {DATABASES['default']['OPTIONS']}")
