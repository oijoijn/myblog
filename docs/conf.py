# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'myblog'
copyright = '2024, M24A22'
author = 'M24A22'
release = '2024/11/21'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',          # 自動ドキュメント生成
    'sphinx.ext.napoleon',         # GoogleやNumPy形式のDocstring対応
    'sphinx.ext.viewcode',         # ソースコードのリンクを表示
    'sphinx_autodoc_typehints',    # 型ヒントのサポート
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'ja'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Read the Docsテーマに変更
html_static_path = ['_static']

# -- Django setup ------------------------------------------------------------
import os
import sys
import django

# Djangoプロジェクトのルートパスを設定
sys.path.insert(0, os.path.abspath('../'))  # Djangoプロジェクトの親ディレクトリを指定
os.environ['DJANGO_SETTINGS_MODULE'] = 'your_project_name.settings'  # プロジェクト名を実際の名前に置き換えてください
django.setup()
