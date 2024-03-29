

from pathlib import Path
import os
import dj_database_url
from datetime import timedelta
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-fh+zkylo9^^&g6y$(2$g_ia(!h96qpsmnc!+mnau=*9favmkd%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'meshackkimutai34@gmail.com'
EMAIL_HOST_PASSWORD = 'mscm ogka yhij bvgy'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'patientapp',
    'multiselectfield',
    'rest_framework',
    'rest_framework_simplejwt',
    'django_twilio',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'patient_portal.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'patient_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, "/media/")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

# Media Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AUTH_USER_MODEL = 'patientapp.Account'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = [
    'patientapp.backends.MyCustomBackend',  
    'django.contrib.auth.backends.ModelBackend',
]

REST_FRAMEWORK = {
   "DEFAULT_PERMISSION_CLASSES": [
       "rest_framework.permissions.AllowAny",
   ],
   "DEFAULT_AUTHENTICATION_CLASSES": (
       "rest_framework_simplejwt.authentication.JWTAuthentication",
   ),
}


SIMPLE_JWT = {
   "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.MyTokenObtainPairSerializer",
   "ACCESS_TOKEN_LIFETIME": timedelta(hours=24),
   "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
   "ROTATE_REFRESH_TOKENS": False,
   "BLACKLIST_AFTER_ROTATION": False,
   "UPDATE_LAST_LOGIN": False,
   "ALGORITHM": "HS256",
   "SIGNING_KEY": SECRET_KEY,
   "VERIFYING_KEY": "",
   "AUDIENCE": None,
   "ISSUER": None,
   "JSON_ENCODER": None,
   "JWK_URL": None,
   "LEEWAY": 0,
   "AUTH_HEADER_TYPES": ("Bearer",),
   "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
   "USER_ID_FIELD": "id",
   "USER_ID_CLAIM": "user_id",
   "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
   "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
   "TOKEN_TYPE_CLAIM": "token_type",
   "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
   "JTI_CLAIM": "jti",
   "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
   "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
   "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
   "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
   "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
   "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
   "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
   "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
   "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
