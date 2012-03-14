from django.contrib import admin

from fpe2aa.models import Platform, AppType, Author, Application

admin.site.register(Platform)
admin.site.register(AppType)
admin.site.register(Author)
admin.site.register(Application)
