from django.conf import settings as django_settings

def settings(request):
    return dict(
        ANALYTICS_CODE = django_settings.ANALYTICS_CODE,
    )
