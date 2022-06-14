from django.db import models
from django.utils import timezone

class ReviewPublishedManger(models.Manager):
    """
    # TODO: 
    """
    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)