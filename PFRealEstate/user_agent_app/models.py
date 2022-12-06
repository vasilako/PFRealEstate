from django.contrib.auth.models import User

from django.db import models
from PFRealEstate.property_app.models import Property_mod


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
        Property_mod,
        on_delete=models.SET_NULL,
        null=True,
    )
