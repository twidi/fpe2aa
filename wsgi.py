import os, sys
SOURCE_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'source'))
sys.path[0:0] = [SOURCE_PATH,]
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
