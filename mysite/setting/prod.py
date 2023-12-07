from mysite.settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0ag5##3m^70x8wg_97$xcc-407gq(fw6$b9ng=^qfhypiyp7r6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# INSTALLED_APPS = []

SITE_ID = 3

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

import pymysql
pymysql.version_info = (1, 4, 3, "final", 0)
pymysql.install_as_MySQLdb()

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
'''
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'nikir_sitedb',
		'USER': 'nikir_nik404',
		'PASSWORD': 'Mn09382783268',
		'HOST':'localhost',
		'PORT':'3306',
	}
}

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

CSRF_COOKIE_SECURE = True


## X-Frame-Options
X_FRAME_OPTIONS = 'DENY'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

SECURE_BROWSER_XSS_FILTER = True