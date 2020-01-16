
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0%!2(ls*#=1+x57lg0&mt=)nr&hljszkwgf*ez8712io7@th!*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'core',
    'user',
    
    
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

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

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'badgeyay',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

SOCIAL_AUTH_GITHUB_KEY = '1d7e54250221b1c58f88'
SOCIAL_AUTH_GITHUB_SECRET = 'ab000125ae547ad29afaaf2fd39704b2e17652b4'

SOCIAL_AUTH_TWITTER_KEY = '94Ka15xHDDitqLQuSaMKphSyz'
SOCIAL_AUTH_TWITTER_SECRET = 'FDI2JPRxkyuPRgXI7yVUV7lWTKN3fhP1sE6cwOP1TEUgpYIUBo'

SOCIAL_AUTH_FACEBOOK_KEY = '1043012449393419'  
SOCIAL_AUTH_FACEBOOK_SECRET = '0618ef833304a5c0ce7612872e98e199'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '6_i5zYkXLrObFoXs_RVj-yM5'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '751522856838-90b7staguo84irrraghaef1mth0g5rav.apps.googleusercontent.com'

SOCIAL_AUTH_RAISE_EXCEPTIONS = False
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'


