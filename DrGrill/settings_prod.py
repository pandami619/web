DEBUG = False
ALLOWED_HOSTS = ['*']

DATEBASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'django_shop',
        'PASSWORD': 'django_shop_test',
        'HOST': 'localhost',
        'PORT': '',
    }
}