
from apk.models import Item,PurchesOrder
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Item)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PurchesOrder.quantity+=1
        PurchesOrder.save()