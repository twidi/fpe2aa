from django.core.management.base import NoArgsCommand

from popularity.models import ViewTracker

from fpe2aa.models import Application


def copy_popularity():

    pop_by_id = dict((v.id, v.popularity) for v in ViewTracker.objects.get_for_model(Application).select_popularity())

    for application in Application.objects.all():
        if application.id in pop_by_id:
            if application.rank != pop_by_id[application.id]:
                print "%s : %s => %s" % (application.slug, application.rank, pop_by_id[application.id])
                application.rank = pop_by_id[application.id]
                application.save()


class Command(NoArgsCommand):
    help = "Copy popularity from django_popularity to rank in fe2aa"

    def handle_noargs(self, **options):
        copy_popularity()
