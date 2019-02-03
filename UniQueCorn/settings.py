"""
Django settings for UniQueCorn project.

Generated by 'django-admin startproject' using Django 1.11.15.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url


if os.environ.get('DEVELOPMENT'):
    development = True
else:
    development = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECRET_KEY = '(f^tzbk_6&i^l(k6)-l(59_3r4v*shml^)0r)s(1kxl&0gq31i'
# The default SECRET_KEY was replaced by environment variables (different for development and production).
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    # "localhost",
    # "0.0.0.0",
    # "127.0.0.1",
    # "unique-corn.herokuapp.com",
    os.environ.get('HOSTNAME'),
    ]

# host = os.environ.get('SITE_HOST')
# if host:
#     ALLOWED_HOSTS.append(host)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'testing',
    'accounts',
    'home'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'UniQueCorn.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'UniQueCorn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if development:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }


# DATABASES = {
#         'default': dj_database_url.parse("postgres://tcqoipytozvlke:0317ac04ecd88e9874ad3cb2c06d75ca417acec39c4b7a9a37d11ab023b3e761@ec2-46-137-170-51.eu-west-1.compute.amazonaws.com:5432/d4cl9o887a7f6b")
#     }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Add custom authentication backend to allow users to login using email instead of username
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# This is needed for working on cloud 9 due to a cookie bug
# We need to override the default message storage
# https://stackoverflow.com/a/34828308/493553
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Print emails to console
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Sending an actual email
# EMAIL_USE_TLS = True # email encryption used by gmail
# EMAIL_HOST = 'smtp.gmail.com' # Protocol used to send emails
# EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS_GMAIL")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD_GMAIL")
# EMAIL_PORT = 587

# Using my email to send emails.
EMAIL_USE_SSL = True  # email encryption used by gmail
EMAIL_HOST = os.environ.get("EMAIL_HOST_WEBADMIN")
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS_WEBADMIN")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD_WEBADMIN")
EMAIL_PORT = os.environ.get("EMAIL_PORT_WEBADMIN")
DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_ADDRESS_WEBADMIN")

