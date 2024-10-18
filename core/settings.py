import os
import configparser
from datetime import timedelta

from pathlib import Path
from string import ascii_lowercase, digits

from .conf.config import *
from .conf.database import *


CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_FOLDER = os.path.normpath(os.path.join(BASE_DIR, 'secret'))
SECRET_FILE = os.path.normpath(os.path.join(BASE_DIR, 'secret/SECRET.key'))

try:
    SECRET_KEY = open(SECRET_FILE).read().strip()
    

except IOError:
    try:
        from django.utils.crypto import get_random_string

        chars = ascii_lowercase + digits + '!@#$%^&*()-_=+'
        SECRET_KEY = get_random_string(50, chars)

        with open(SECRET_FILE, 'w') as f:
            f.write(SECRET_KEY)
    except IOError:
        raise Exception(f'Не удается открыть {SECRET_FILE}')


DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'rest_framework',

    
    'rest_framework_simplejwt',
    'djoser',
    'api',
    # 'rest_framework.authtoken',

    'drf_yasg',
    'import_export',

    'apps.contents',
] + DEFAULT_INSTALLED_APPS

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


MIDDLEWARE = [

] + DEFAULT_MIDDLEWARE


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

DJOSER = {
    'LOGIN_FIELD': 'username',
    'TOKEN_MODEL': 'rest_framework_simplejwt.token_blacklist.models.BlacklistedToken',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Время жизни access токена
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Время жизни refresh токена
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',  # Алгоритм, который будет использоваться для подписи токена
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),  # Тип заголовка авторизации
}


ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


LANGUAGE_CODE = CONFIG['Django']['LANGUAGE_CODE']

TIME_ZONE = CONFIG['Django']['TIME_ZONE']

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles/'

STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
