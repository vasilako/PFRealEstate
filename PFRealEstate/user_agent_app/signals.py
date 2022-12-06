from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

from PFRealEstate.user_agent_app.models import UserAgent_mod

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_agent_mod(sender, instance, created, **kwargs):
    if created:
        UserAgent_mod.objects.create(UserModel)


@receiver(post_save,sender=UserModel)
def save_user_agent_mod(sender, instance, **kwargs):
    instance.UserAgent_mod.save()

