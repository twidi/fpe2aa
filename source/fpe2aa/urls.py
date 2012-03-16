from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from fpe2aa.models import AppType, Platform, Author, Application

urlpatterns = patterns('',
    url(r'^types/$', ListView.as_view(model=AppType), name='type_list'),
    url(r'^type/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=AppType), name='type_detail'),

    url(r'^plateformes/$', ListView.as_view(model=Platform), name='platform_list'),
    url(r'^plateforme/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Platform), name='platform_detail'),

    url(r'^auteurs/$', ListView.as_view(model=Author), name='author_list'),
    url(r'^auteur/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Author), name='author_detail'),

    url(r'^applications/$', ListView.as_view(model=Application), name='application_list'),
    url(r'^(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Application), name='application_detail'),
)

