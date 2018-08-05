DEBUG = False
ALLOWED_HOSTS = ['*']

DATEBASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'drgrill',
        'PASSWORD': 'Lock099312',
        'HOST': 'localhost',
        'PORT': '',
    }
}