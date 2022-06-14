from django.db import models

from apps.core.models.base import Authorable, Timestampable


class Tag(Authorable, Timestampable):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'stackoverflow_tags'
