from .base import *
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = [
    # e.g. 'micro.domains', 'www.micro.domains'
    'sell-everything.herokuapp.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USERNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}

# HTTPS Settings
SESSION_COOKIE_SECURE = True # https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/#session-cookie-secure
CSRF_COOKIE_SECURE = True # https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/#csrf-cookie-secure
SECURE_SSL_REDIRECT = True # Make sure your all traffic are redirected from http to https

# HSTS (Http Strict Transport Security) Settings
# Adding some information to header of request which says browser can't access without using https connection
SECURE_HSTS_SECONDS = 31536000 # 1 year
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# so your pages will not be served with an 'x-content-type-options: nosniff' header. You should consider enabling this header to prevent the browser from identifying content types incorrectly.
SECURE_CONTENT_TYPE_NOSNIFF = True
# so your pages will not be served with an 'x-xss-protection: 1; mode=block' header. You should consider enabling this header to activate the browser's XSS filtering and help prevent XSS attacks.
SECURE_BROWSER_XSS_FILTER = True
# The default is 'SAMEORIGIN', but unless there is a good reason for your site to serve other parts of itself in a frame, you should change it to 'DENY'.
X_FRAME_OPTIONS = 'DENY'