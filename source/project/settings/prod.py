DEBUG = False
TEMPLATE_DEBUG = False

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


