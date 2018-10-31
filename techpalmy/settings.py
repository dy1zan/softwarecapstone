"""
Django settings for techpalmy project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/

Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

"""

import os
from django.contrib import messages


# ==============================================================================
# General
# ==============================================================================
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SECRET_KEY = 'xhq-$*w#$ggbdi8pz(f=de^82dcf+_d-@exfgze&h!u2y=#scg'

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]

# django.urls
ROOT_URLCONF = 'techpalmy.urls'

# django.contrib.auth
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/login/'

# ------------------------------------------------------------------------------
# Database
# When DEBUG is True, Development MySQL details are used.
# When DEBUG is False, Production MySQL details are used.
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
# ------------------------------------------------------------------------------
if DEBUG == True:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'NAME': 'techpalmy',
            'USER': 'techpalmy',
            'PASSWORD': 'rubberducky',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'NAME': 'techpalmy',
            'USER': 'techpalmy',
            'PASSWORD': 'rubberducky',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True



# ==============================================================================
# Paths
# ==============================================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files (e.g apps/myapp/static).
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media files (e.g user avatars)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



# ==============================================================================
# Installed Apps
# ==============================================================================

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.humanize',
    'widget_tweaks',
    'debug_toolbar',
    'django_filters',
    'ckeditor',
    'captcha',
]

PROJECT_APPS = [
    'apps.user',
    'apps.jobs',
    'apps.event',
    'apps.entity',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]



# ==============================================================================
# Plugin related configuration
#   SECURITY WARNING: Keep all secret keys (or private keys) secret at all times.
# ==============================================================================
# ------------------------------------------------------------------------------
# captcha
# ------------------------------------------------------------------------------
RECAPTCHA_PRIVATE_KEY = "6LeGinEUAAAAACOfUF3UvjkMODVlTBUtrsToio6C"
RECAPTCHA_PUBLIC_KEY = "6LeGinEUAAAAADHfruk8yQcqD_cOXMWseI0CFV79"
NOCAPTCHA = True

# ------------------------------------------------------------------------------
# debug_toolbar
# ------------------------------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

# ------------------------------------------------------------------------------
# ckeditor
# ------------------------------------------------------------------------------
CKEDITOR_BASEPATH = os.path.join(STATIC_URL, 'ckeditor/ckeditor/')
CKEDITOR_CONFIGS = {
    'default': {
        'uiColour': '#343A40',
        'width': '100%',
        'height': '20.6vh',
        'skin': 'moono-dark',
        'toolbar_Basic': [
            ['Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Blockquote', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight']},
            {'name': 'links', 'items': ['Link', 'Unlink']},
            {'name': 'insert',
             'items': ['Image', 'Table', 'HorizontalRule']},
       
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            # your extra plugins here
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
        ]),
    }
}

# ------------------------------------------------------------------------------
# django.contrib.messages
# ------------------------------------------------------------------------------
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}



# ==============================================================================
# Misc
# ==============================================================================

# django templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],

            'libraries': {
                'startswith': 'techpalmy.templatetags.startswith',
            }
        },
    },
]

WSGI_APPLICATION = 'techpalmy.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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




