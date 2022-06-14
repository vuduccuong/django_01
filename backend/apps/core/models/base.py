from django.db import models
from django.contrib.auth.models import User


class Timestampable(models.Model):
    """
    Abstract base class model that providers self-updating `created` and `modified`
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Publishable(models.Model):
    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Authorable(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class Permalinkable(models.Model):

    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True

    def get_url_kwargs(self, **kwargs):
        kwargs.update(getattr('url_kwargs', {}))
        return kwargs

    def get_absolute_url(self):
        url_kwargs = self.get_url_kwargs(slug=self.slug)
        return (self.url_name, (), url_kwargs)

    def pre_save(self, instance, add):
        from django.utils.text import slugify
        if not instance.slug:
            instance.slug = slugify(self.slug_source)
