from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import ListView
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from fpe2aa.models import Application
from fpe2aa.urls import online_applications_queryset

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Application, queryset=online_applications_queryset, template_name='home.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^a-propos/', direct_to_template, { 'template': 'about.html', 'extra_context': dict(section='about') }, name="about"),
    url(r'^viewtracker/', include('popularity.urls')),
    url(r'^', include('fpe2aa.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
