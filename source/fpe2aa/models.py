import os

from django.db import models

from easy_thumbnails.fields import ThumbnailerImageField

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

def image_name_from_slug(base_dir):
    """
    Function to use for "upload_to" of an ImageField, passing a
    base directory which will be added after MEDIA_ROOT
    """
    def inner_func(instance, filename):
        return os.path.join(
                base_dir,
                u''.join(
                    [ instance.slug, os.path.splitext(filename)[1] ]
                )
            )
    return inner_func

class Author(models.Model):
    """
    An author of an application. Linked via Application with a M2M
    For instance: Liberation, Owni...
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, help_text="For the Author's url")
    link = models.URLField()
    logo = ThumbnailerImageField(null=True, blank=True,
            upload_to=image_name_from_slug('logo'),
            resize_source=dict(size=(70, 0), crop='smart'),
        )

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
    screenshot = ThumbnailerImageField(null=True, blank=True,
            upload_to=image_name_from_slug('screenshots'),
            resize_source=dict(size=(1170, 0), crop='smart'),
        )

    def __unicode__(self):
        return self.name

