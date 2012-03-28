from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from fpe2aa.models import Application, Author, AppType, Platform

class ApplicationsView(ListView):
    context_object_name = 'applications'
    model = Application

    def get_queryset(self):
        qs = self.model.online_only.all()

        self._sort = self.request.GET.get('sort', '')
        if self._sort == 'name':
            qs = qs.order_by('slug')
        elif self._sort == 'date':
            qs = qs.order_by('-date_add')
        else:
            self._sort = None

        return qs

    def get_context_data(self, **kwargs):
        context = super(ApplicationsView, self).get_context_data(**kwargs)
        context['sort'] = self._sort
        return context

class AuthorView(ApplicationsView):

    def get_queryset(self):
        self._author = get_object_or_404(Author, slug=self.kwargs['slug'])
        qs = super(AuthorView, self).get_queryset()
        return qs.filter(authors=self._author)

    def get_context_data(self, **kwargs):
        context = super(AuthorView, self).get_context_data(**kwargs)
        context['author'] = self._author
        return context

class AppTypeView(ApplicationsView):

    def get_queryset(self):
        self._apptype = get_object_or_404(AppType, slug=self.kwargs['slug'])
        qs = super(AppTypeView, self).get_queryset()
        return qs.filter(types=self._apptype)

    def get_context_data(self, **kwargs):
        context = super(AppTypeView, self).get_context_data(**kwargs)
        context['type'] = self._apptype
        return context

class PlatformView(ApplicationsView):

    def get_queryset(self):
        self._platform = get_object_or_404(Platform, slug=self.kwargs['slug'])
        qs = super(PlatformView, self).get_queryset()
        return qs.filter(platforms=self._platform)

    def get_context_data(self, **kwargs):
        context = super(PlatformView, self).get_context_data(**kwargs)
        context['platform'] = self._platform
        return context
