#
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
)

#ANALYTICS_CODE = "test";

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pa_dev',
        'USER': 'pa_dev',
        'PASSWORD': 'pa_dev',
    }
}

POPULARITY_COMPATABILITY_OVERRIDE = (DATABASES['default']['ENGINE'],)
