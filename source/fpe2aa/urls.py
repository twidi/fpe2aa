from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from fpe2aa.models import AppType, Platform, Author, Application

urlpatterns = patterns('',
    url(r'^type/$', ListView.as_view(model=AppType), name='type_list'),
    url(r'^type/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=AppType), name='type_detail'),

    url(r'^plateforme/$', ListView.as_view(model=Platform), name='plateform_list'),
    url(r'^plateforme/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Platform), name='platform_detail'),

    url(r'^auteur/$', ListView.as_view(model=Author), name='author_list'),
    url(r'^auteur/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Author), name='author_detail'),

    url(r'^$', ListView.as_view(model=Application), name='application_list'),
    url(r'^(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Application), name='application_detail'),
)

