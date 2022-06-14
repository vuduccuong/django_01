from django.db.models import Q
from apps.reviews.models import FlavorReview


class ReviewService:
    def list(self, **kwargs):
        keyword = kwargs.get('keyword', '')
        ft = Q()
        if keyword:
            ft |= Q(review__startswith=keyword) | Q(review__icontains=keyword)
        # Don't do this
        qs_1 = FlavorReview.objects.active().filter(ft).exclude().include()

        # Do this: good for debug, review
        qs_2 = FlavorReview.objects.active()
        qs_2 = qs_2.filter(ft)
        qs_2 = qs_2.exclude()
        qs_2 = qs_2.include()

        # Beauty: Chaining Queries: for review, not good for debug
        qs_3 = (
            FlavorReview
            .objects
            .active()
            .filter(ft)
            .exclude()
            .include()
        )
