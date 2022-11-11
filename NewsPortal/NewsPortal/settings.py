from  pathlib import Path
import os
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)0!asuo@g@+*ob)vm@u)gerlcnk0)!ifbnfw)fh@mcoh-4sg2e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news.apps.NewsConfig',
    'fpages',
    'accounts',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django_apscheduler',


]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

]

ROOT_URLCONF = 'NewsPortal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
   'django.contrib.auth.backends.ModelBackend',
   'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'NewsPortal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {'signup': 'sign.models.CommonSignupForm'}

SITE_URL = 'http://127.0.0.1:8000'

load_dotenv(find_dotenv())

EMAIL_HOST = 'smtp.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

APSCHEDULER_DATETIME = 'N j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 10

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

LOGGING = {
    'version': 1,
    'disable_existing_logger': False,
    'formatters': {
        #INFO format
        'in_format': {
            'style': '{',
            'format': '{asctime} | {levelname} | {modul} | {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
        },
        #debug format
        'de_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {levelname} | {message}',
        },
        #warning format
        'w_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {leveltime} | {pathname} | {exc_info} | {message}',
        },
        #error and critical formet
        'error_critical_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {levelname} | {pathname} | {exc_info} | {message}',
        },
        'mail_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {leveltime} | {pathname} | {message}',
        },
        'security_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {leveltime} | {modul} | {message}',
        },
        'general_log_format': {
            'style': '{',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'format': '{asctime} | {leveltime} | {modul} | {message}',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
            #обраб когда DEBUG=False в setting.py
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        },
    },
    'handlers': {
        'console_i': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'in_format',
        },
        'console_d': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'de_format',
        },
        'console_w': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'w_format',
        },
        'console_error_critical': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'error_critical_format',
        },
        'general_file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'formatter': 'general_log_format',
        },
        'errors_file': {
            'class': 'logging.FileHandler',
            'filename': 'errors.log',
            'level': 'ERROR',
            'formatter': 'error_critical_format',
        },
        'security_file': {
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'level': 'WARNING',
            'formatter': 'security_format',
        },
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'formatter': 'mail_format',
        },
    },
    'loggers': {
        'console_debug': {
            'handlers': ['console_d'],
            'propagate': True,
        },
        'console_warning': {
            'handlers': ['console_w'],
            'propagate': True,
        },
        'console_error': {
            'handlers': ['console_error_critical'],
            'propagate': True,
        },
        'django.reguest': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mail_admins', 'errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django_db_backends': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors_file'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security_file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}
