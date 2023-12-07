from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0ag5##3m^70x8wg_97$xcc-407gq(fw6$b9ng=^qfhypiyp7r6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# INSTALLED_APPS = []

SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

X_FRAME_OPTIONS = 'SAMEORIGIN'
'''
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT ##django compressor
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED: ##django compressor
COMPRESS_ENABLED = True
COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"] ##django compressor
'''