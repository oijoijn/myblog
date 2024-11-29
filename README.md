## 1 myblog
#### 1 目的
        面白そうな技術や触ったことのある技術を紹介するサイト
#### 2 URL
        https://technologicalexploration.pythonanywhere.com/blog/

#### 4 機能要件(CRUD処理◦会員機能)
        会員機能
        コメント機能
        コメント編集機能

#### 5 非機能要件
        データベースで保存するもの
            accounts:
                ニックネーム
                パスワードをハッシュ化したものを保存
            blog:
                ブログのタイトル
                ブログのpath
                ブログのイメージ画像

## 2 設計◦仕様書

## 3 主要技術
|使用言語・フレームワーク|バージョン|
|------------------------|----------|
|Python                  | 3.8      |
|Django                  | 4.2.16   |
|Mysql                   | 8.0      |


|インフラ       |バージョン     |
|---------------|---------------|
|Pythonanywhere |               |
|Docker         |27.2.0         |
|Shell Script   |               |

## 4 コマンド一覧

|コマンド                                   | 処理                          |
|------------------------------------------|-------------------------------|
|docker compose up -d                      |コンテナをバックエンドで実行   |
|docker compose down                       |コンテナを停止と削除           |
|docker exec -it myblog-django-1 /bin/bash |コンテナに仮想端末を割り当てる |
|winpty docker exec -it myblog-django-1 //bin//bash |git bashを使用している場合     |
|docker exec -it myblog-mysql-1 mysql -u root -p|mysqlコンテナに接続|
|bash setup_env.sh r                       |djangoのサーバを起動           |
|bash setup_env.sh s                       |データベースのマイグレーション            |
|bash setup_env.sh rms                       |データベースの削除            |
|bash setup_env.sh c                       |rootユーザの作成           |

## 5 ディレクトリ構成

```
.
├── Dockerfile
├── README.md
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docker-compose.yml
├── error.txt
├── manage.py
├── media
│   └── images
│       └── test_AEifLKY.png
├── myblog
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── test_settings.py
│   ├── urls.py
│   └── wsgi.py
├── requirements.txt
├── setup_env.sh
├── static
│   ├── css
│   │   └── style.css
│   ├── gif
│   │   └── key
│   │       └── key.gif
│   ├── images
│   │   ├── docker
│   │   │   ├── docker-logo.png
│   │   │   ├── docker_tutorial_1.png
│   │   │   ├── docker_tutorial_2.png
│   │   │   ├── docker_tutorial_3.png
│   │   │   └── docker_tutorial_4.png
│   │   ├── key
│   │   │   └── keyboard.png
│   │   ├── myblog
│   │   │   └── Pangolin.png
│   │   └── padding.py
│   └── js
│       └── script.js
└── templates
    ├── accounts
    │   ├── login.html
    │   ├── signup.html
    │   ├── user_comments.html
    │   └── user_update.html
    ├── base.html
    ├── blog
    │   ├── article.html
    │   ├── comments.html
    │   ├── docker_tutorial_1.html
    │   ├── edit_comment.html
    │   ├── home.html
    │   └── key.html
    └── index.html

20 directories, 57 files
```
