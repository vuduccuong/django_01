from django.db import models

from apps.core.models.base import Timestampable, Publishable, Permalinkable, Authorable
from .tag import Tag


class Question(Authorable, Timestampable, Publishable, Permalinkable):
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')

    class Meta:
        db_table = 'stackoverflow_questions'

    @property
    def slug_source(self):
        return self.title
