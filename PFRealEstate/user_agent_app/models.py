# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# UserModel = get_user_model()

class UserAgent_mod(AbstractUser):

    phone_number = models.CharField(
        max_length=9,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        upload_to='photos_user_agent',
    )

    # manage_properties = models.ManyToManyField(
    #     to='property_app.Property_mod',
    #     related_name='manage_properties',
    #     blank=True
    #
    # )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name='Admin - Agent -User'
        verbose_name_plural = 'Admins - Agents- Users'



#---------------------------------------------------------------------------------
# class UserAgent_mod(models.Model):
#     user = models.OneToOneField(
#         UserModel,
#         on_delete=models.CASCADE,
#         primary_key=True
#
#     )
#     phone_number = models.CharField(
#         max_length=9,
#         blank=True,
#         null=True,
#     )
#     profile_image = models.ImageField(
#         upload_to='photos_user_agent',
#     )
#
#     def __str__(self):
#         make_name = str(self.user)
#         return make_name
#
#     class Meta:
#         verbose_name='Agent'
#         verbose_name_plural = 'Agents'
#
#
#     # manage_properties = models.ManyToManyField(
#     #     to='property_app.Property_mod',
#     #     related_name='manage_properties'
#     # )
#     #
#     # @property
#     # def number_of_properties(self):
#     #     all_propertis = self.manage_properties.objects.all()
#     #     return len(all_propertis)
#
#
#
# # from django.dispatch import receiver
# # from django.db.models.signals import post_save
# #
# # @receiver(post_save, sender=UserModel)
# # def update_user_agent_mod(sender, instance, created, **kwargs):
# #     if created:
# #         UserAgent_mod.objects.create(UserModel=instance)
# #     instance.UserAgent_mod.save()



