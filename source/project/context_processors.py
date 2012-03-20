from django.conf import settings as django_settings
from django.contrib.contenttypes.models import ContentType

from fpe2aa.models import Application

def settings(request):
    return dict(
        ANALYTICS_CODE = django_settings.ANALYTICS_CODE,
        APP_CID = ContentType.objects.get_for_model(Application).id,
    )
