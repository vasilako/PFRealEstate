from django.contrib.auth import get_user_model

from django.db import models

UserModel = get_user_model()
class UserAgent_mod(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,

    )
    phone_number = models.CharField(
        max_length=9,
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='photos_user_agent',
    )

    def __str__(self):
        make_name = str(self.user)
        return make_name

    class Meta:
        verbose_name='Agent'
        verbose_name_plural = 'Agents'


    # manage_properties = models.ManyToManyField(
    #     to='property_app.Property_mod',
    #     related_name='manage_properties'
    # )
    #
    # @property
    # def number_of_properties(self):
    #     all_propertis = self.manage_properties.objects.all()
    #     return len(all_propertis)



