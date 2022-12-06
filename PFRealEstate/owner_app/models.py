from django.db import models


# Create your models here.
class Owner_mod(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank= False,
    )

    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    phone_number = models.PositiveIntegerField(
        verbose_name= 'Owner phone',
        null=False,
        blank=False

    )

    owner_properties = models.ForeignKey(
        to='property_app.Property_mod',
        on_delete=models.CASCADE,
        # De este modo se evita el Impot del modelo porque ya es un string
        related_name='owner_properties',
        blank=True,
        verbose_name = 'Owner Properties',
    )

