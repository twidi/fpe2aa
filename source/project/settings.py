# Django settings for project project.

import django.conf.global_settings as DEFAULT_SETTINGS
import os, sys

PROJECT_PATH = os.path.dirname(__file__)
BASE_PATH = os.path.normpath(os.path.join(PROJECT_PATH, '../'))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                         # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.normpath(os.path.join(BASE_PATH, 'db.sqlite')), # Or path to database file if using sqlite3.
        'USER': '',                                                     # Not used with sqlite3.
        'PASSWORD': '',                                                 # Not used with sqlite3.
        'HOST': '',                                                     # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                                     # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.normpath(os.path.join(PROJECT_PATH, 'static')),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-gaj*uhuv7e@v#214&amp;u+d4k7rsem%!pzo2w1^%5tr_fw)eoc!!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'johnny.middleware.LocalStoreClearMiddleware',
    'johnny.middleware.QueryCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.normpath(os.path.join(PROJECT_PATH, 'templates')),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django.contrib.staticfiles',
    'django_extensions',
    'easy_thumbnails',
    'popularity',
    'fpe2aa',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'project.context_processors.settings',
    'fpe2aa.context_processors.filters',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# caching
CACHES = {
    'default': dict(
        BACKEND = 'django.core.cache.backends.locmem.LocMemCache',
        LOCATION = 'default',
    ),
    'johnny': dict(
        BACKEND = 'johnny.backends.locmem.LocMemCache',
        LOCATION = 'johnny',
        JOHNNY_CACHE = True,
    ),
}
JOHNNY_MIDDLEWARE_KEY_PREFIX='jc'


# thumbnails
THUMBNAIL_SUBDIR = 'thumbs'
THUMBNAIL_EXTENSION = 'png'

# other
ANALYTICS_CODE = None

# metasettings
try:
    import metasettings
    METASETTINGS_DIR    = os.path.normpath(os.path.join(PROJECT_PATH, 'settings'))
    try:
        from settings_rules import method, rules
    except ImportError, e:
        raise e
    else:
        METASETTINGS_PATTERNS = rules
        METASETTINGS_METHOD = getattr(metasettings, method)
        metasettings.init(globals())
except Exception, e:
    sys.stderr.write("Error while loading metasettings : %s\n" % e )
    try:
        from local_settings import *
    except ImportError, e:
        sys.stderr.write("Error: You should define your own settings, see settings_rules.py.sample (or just add a local_settings.py)\nError was : %s\n" % e)
        sys.exit(1)

