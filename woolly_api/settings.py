"""
Django settings for woolly_api project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from woolly_api import settings_confidential as confidentials


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# 		SECRET KEYS
# --------------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = confidentials.SECRET_KEY

# CAS config
CAS_SERVER_URL = 'https://cas.utc.fr/cas/'
CAS_LOGOUT_COMPLETELY = True
CAS_PROVIDE_URL_TO_LOGOUT = True
CAS_AUTO_CREATE_USER = True
CAS_RESPONSE_CALLBACKS = (
	'authentication.backends.loggedCas',
)

# Ginger config
GINGER_KEY = confidentials.GINGER_KEY
GINGER_SERVER_URL = 'https://assos.utc.fr/ginger/v1/'

# Payutc config
PAYUTC_KEY = confidentials.PAYUTC_KEY

# Portail des Assos config
PORTAL = {
	'oauth': {
		'client_id': 		confidentials.PORTAL['id'],
		'client_secret': 	confidentials.PORTAL['key'],
		'base_url': 		'https://portail-assos.alwaysdata.net/api/v1/',
		'authorize_url': 	'https://portail-assos.alwaysdata.net/oauth/authorize',
		'access_token_url': 'https://portail-assos.alwaysdata.net/oauth/token',
		'redirect_uri': 	'http://localhost:8000/auth/callback',
		'scope': 			'user-get-assos-done-now user-get-info'
	}
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# CORS headers config
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
)

# necessary in addition to the whitelist for protected requests
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = (
	"localhost"
)


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
	'default': confidentials.DATABASE,
	'sqlite': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': 'db',
	}
}


# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',		# Utile ?
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'cas',
	'corsheaders',
	'core',
	'authentication',
	'sales',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'cas.middleware.CASMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'woolly_api.urls'

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
			],
		},
	},
]

WSGI_APPLICATION = 'woolly_api.wsgi.application'


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

AUTH_USER_MODEL = 'authentication.WoollyUser'

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

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'authentication.backends.GingerCASBackend',
)

REST_FRAMEWORK = {
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
	),
	'PAGE_SIZE': 10,
	'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
	'DEFAULT_PAGINATION_CLASS':
		'rest_framework_json_api.pagination.PageNumberPagination',
	'DEFAULT_PARSER_CLASSES': (
		'rest_framework_json_api.parsers.JSONParser',
		'rest_framework.parsers.FormParser',
		'rest_framework.parsers.MultiPartParser'
	),
	'DEFAULT_RENDERER_CLASSES': (
		'rest_framework_json_api.renderers.JSONRenderer',
		'rest_framework.renderers.BrowsableAPIRenderer',
	),
	'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
}
