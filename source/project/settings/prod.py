DEBUG = False
TEMPLATE_DEBUG = False
PROD = True

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

ADMINS = (
    ('Twidi', 's.angel+presid-apps@twidi.com'),
)
MANAGERS = ADMINS

THUMBNAIL_MEDIA_URL = 'http://thumb.presid-apps.fr/media/'
STATIC_URL_JS = 'http://js.static.presid-apps.fr/static/'
STATIC_URL_CSS = 'http://css.static.presid-apps.fr/static/'

