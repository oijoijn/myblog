import os
import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")

STATIC_DIR = Path.joinpath(BASE_DIR, env("STATIC_DIR"))
STATIC_URL = env('STATIC_URL')
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS =[
    STATIC_DIR,
]

print(f'STATIC_DIR: {STATIC_DIR}')
print(f'STATIC_URL: {STATIC_URL}')
print(f'STATIC_ROOT: {STATIC_ROOT}')