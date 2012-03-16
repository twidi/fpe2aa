from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from fpe2aa.models import Application

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Application, template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('fpe2aa.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
