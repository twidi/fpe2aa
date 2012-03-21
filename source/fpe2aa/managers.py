from django.db import models

class OnlineApplicationsManager(models.Manager):
    """
    A manager to return only applications marked as "online"
    """

    def get_query_set(self):
        qs = super(OnlineApplicationsManager, self).get_query_set()
        qs = qs.prefetch_related('authors', 'types', 'platforms')
        return qs.filter(online=True)
