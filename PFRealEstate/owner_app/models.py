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

    phone_number = models.CharField(
        verbose_name= 'Owner phone',
        max_length=9,
        null=False,
        blank=False

    )

    owner_properties = models.ManyToManyField(
        to='property_app.Property_mod',
        # De este modo se evita el Impot del modelo porque ya es un string
        related_name='owner_properties',
        blank=True,
        verbose_name = 'Owner Properties',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name = 'Owner'
        verbose_name_plural ='Owners'
        ordering = ['first_name', 'last_name']


