from fpe2aa.models import Author, Platform, AppType

def filters(request):
    """
    Return list of all filterable objects to easy access in templates
    """
    filter_type = None
    filter = None

    if request.path.startswith('/auteur/'):
        filter_type = 'author'
    elif request.path.startswith('/plateforme/'):
        filter_type = 'platform'
    elif request.path.startswith('/type/'):
        filter_type = 'type'
    elif request.path in ('/', '/applications/'):
        filter_type = 'all'

    if filter_type and filter_type != 'all':
        try:
            filter = request.path.split('/')[2]
        except:
            pass

    return dict(
        authors = Author.objects.all(),
        platforms = Platform.objects.all(),
        types = AppType.objects.all(),
        filter_type = filter_type,
        filter = filter,
    )
