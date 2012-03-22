import json
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'template1',
        'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
        'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
        'HOST': env['DOTCLOUD_DB_SQL_HOST'],
        'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
    }
}

MEDIA_ROOT = '/home/dotcloud/data/media/'

SECRET_KEY = env.get('DJANGO_SECRET_KEY', 'presidc)u6kx&j*q*dx@!-38q3t99)7q64x*y9^8i881ssse4!^&64tdapps')

ANALYTICS_CODE = env.get('ANALYTICS_CODE', ANALYTICS_CODE)


