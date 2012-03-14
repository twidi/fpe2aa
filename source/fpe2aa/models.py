from django.db import models

class Platform(models.Model):
    """
    A platform where an application can be found. Linked via Application with
    a M2M.
    For instance: iPhone, Android, Web...
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text="For the Platform's url")

    def __unicode__(self):
        return self.name


class AppType(models.Model):
    """
    A type of an application. Linked via Application with a M2M.
    For instance: sondage, analyse, test...
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text="For the AppType's url")

    def __unicode__(self):
        return self.name


class Author(models.Model):
    """
    An author of an application. Linked via Application with a M2M
    For instance: Liberation, Owni...
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text="For the Author's url")
    link = models.URLField()

    def __unicode__(self):
        return self.name


class Application(models.Model):
    """
    An application with mainly a name and a link. Can have many authors and
    types
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
            help_text="For the Application's url")
    description = models.TextField()
    link = models.URLField()
    authors = models.ManyToManyField(Author, null=True, blank=True)
    online = models.BooleanField(default=True,
            help_text="Set to False to remove this Application from the front")
    date_add = models.DateTimeField(auto_now_add=True)
    platforms = models.ManyToManyField(Platform, null=True, blank=True)
    types = models.ManyToManyField(AppType, null=True, blank=True)
    screenshot = models.ImageField(null=True, blank=True, upload_to='screeshots/')

    def __unicode__(self):
        return self.name

