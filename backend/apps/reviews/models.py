from django.db import models

from apps.reviews.managements.published import ReviewPublishedManger
from apps.core.models.base import Timestampable, Publishable

class FlavorReview(Timestampable, Publishable):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    # add customer manager
    objects = ReviewPublishedManger()

    class Meta:
        db_table = 'c-reviews'
