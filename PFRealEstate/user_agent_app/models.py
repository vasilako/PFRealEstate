from django.contrib.auth.models import User

from django.db import models


# Create your models here.
class UserAgent_mod(models.Model):
    user = models.OneToOneField(
        User,
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


    manage_properties = models.ForeignKey(
        to='property_app.Property_mod',
        on_delete=models.SET_NULL,
        null=True,
    )

    @property
    def number_of_properties(self):
        all_propertis = self.manage_properties
        return len(all_propertis)

