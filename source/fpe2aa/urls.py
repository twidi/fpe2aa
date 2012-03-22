from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from fpe2aa.models import AppType, Platform, Author, Application

online_applications_queryset = Application.online_only.all()

urlpatterns = patterns('',
    url(r'^categorie/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=AppType), name='type_detail'),
    url(r'^plateforme/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Platform), name='platform_detail'),
    url(r'^auteur/(?P<slug>[\w\/\-]+)/$', DetailView.as_view(model=Author), name='author_detail'),
    url(r'^applications/$', ListView.as_view(model=Application, queryset=online_applications_queryset), name='application_list'),
)

