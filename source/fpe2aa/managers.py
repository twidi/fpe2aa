from django.db import models

class LowerNameMOrderedanager(models.Manager):
    """
    This manager will order queryset by lowercase name by default.
    """

    def get_query_set(self):
        qs = super(LowerNameMOrderedanager, self).get_query_set()
        return qs.extra(
            select = dict(
                lower_name = 'lower(name)',
            ),
        ).order_by('lower_name')
