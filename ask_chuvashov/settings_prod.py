DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_supreme',
        'PASSWORD': 'supreme02v',
        'HOST': 'localhost',
        'PORT': '',
    }
}