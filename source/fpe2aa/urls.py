from django.conf.urls import patterns, url
from fpe2aa.views import AppTypeView, AuthorView, PlatformView, ApplicationsView

urlpatterns = patterns('',
    url(r'^categorie/(?P<slug>[\w\/\-]+)/$', AppTypeView.as_view(), name='type_detail'),
    url(r'^plateforme/(?P<slug>[\w\/\-]+)/$', PlatformView.as_view(), name='platform_detail'),
    url(r'^auteur/(?P<slug>[\w\/\-]+)/$', AuthorView.as_view(), name='author_detail'),
    url(r'^applications/$', ApplicationsView.as_view(), name='application_list'),
)

