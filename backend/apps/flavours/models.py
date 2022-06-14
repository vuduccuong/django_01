import imp
from django.db import models

from apps.core.models.base import Timestampable

class Flavour(Timestampable):
    title = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        db_table = 'c-flavours'