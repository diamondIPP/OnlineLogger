"""
Django settings for the logger project.
"""

from os.path import dirname, abspath, join

BASE_DIR = dirname(dirname(abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o#$le!e2m84oz0#fbnsw4o@lzly5&n(48d&ts*6ra2ptg@21sk'

DEBUG = True  # SECURITY WARNING: don't run with debug turned on in production!

# Application definition
default_apps = [f'django.contrib.{i}' for i in ['admin', 'auth', 'contenttypes', 'sessions', 'messages', 'staticfiles']]
INSTALLED_APPS = ['logger.apps.LoggerConfig'] + default_apps

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'log.wsgi.application'


# Database (https://docs.djangoproject.com/en/1.8/ref/settings/#databases)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Zurich'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = ['0.0.0.0', '192.168.1.103', 'localhost', '127.0.0.1', '192.168.1.100', '192.168.1.5', '192.168.1.111']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
STATIC_URL = '/static/'
