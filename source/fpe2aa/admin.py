from django.contrib import admin

from fpe2aa.models import Platform, AppType, Author, Application

class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class PlatformAdmin(BaseAdmin):
    pass

class AppTypeAdmin(BaseAdmin):
    pass

class AuthorAdmin(BaseAdmin):
    pass

class ApplicationAdmin(BaseAdmin):
    pass

admin.site.register(Platform, PlatformAdmin)
admin.site.register(AppType, AppTypeAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Application, ApplicationAdmin)
