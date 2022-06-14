from django.db import models
from apps.core.constants.flavours_const import Favours as FavourConst
from apps.core.models.base import Timestampable


class IceCreamOrder(Timestampable):
    # 1: Using Tuple -> < Django v3.0 (Recommend)
    flavors_1 = models.CharField(max_length=2, choices=FavourConst.CHOICES)
    # qs: IceCreamOrder.objects.filter(flavors=FavourConst.CHOCOLATE)
     
    # 2: Enum-Based Choice Model Attributes > Django v3.0
    class Flavors(models.TextChoices):
        CHOCOLATE = 'ch', 'Chocolate'
        VANILLA = 'vn', 'Vanilla'
        STRAWBERRY = 'st', 'Strawberry'
        CHUNKY_MUNKY = 'cm', 'Chunky Munky'

    flavors_2 = models.CharField(max_length=2, choices=Flavors.choices)
    # qs: IceCreamOrder.objects.filter(flavors=IceCreamOrder.Flavors.CHOCOLATE)

    class Meta:
        db_table = 'c-orders'