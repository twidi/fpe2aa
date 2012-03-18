from fpe2aa.models import Author, Platform, AppType

def filters(request):
    """
    Return list of all filterable objects to easy access in templates
    """
    return dict(
        authors = Author.objects.all(),
        platforms = Platform.objects.all(),
        types = AppType.objects.all(),
    )
