from django.db import models

class Images_mod(models.Model):
    filename = models.ImageField(
        upload_to=None,
        width_field=300,

    )


class Property_mod(models.Model):
    PROPERTY_TYPES = [
        ('flat', 'Flat'),
        ('area', 'Area'),
        ('chalet', 'Chalet'),
        ('shop', 'Comercial'),
        ('offices', 'Offices'),
    ]

    PROPERTY_OPERATION = [
        ('rent', 'Rent'),
        ('buy', 'Buy'),
    ]

    PROPERTY_STATE = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    type = models.CharField(
        verbose_name='Property Type',
        max_length=7, choices= PROPERTY_TYPES,
        null=False,
        blank=False,
    )

    operation = models.CharField(
        verbose_name='Operation Type',
        max_length=4, choices= PROPERTY_OPERATION,
        null=False,
        blank=False,
    )

    state = models.CharField(
        verbose_name='Property state',
        max_length=4, choices= PROPERTY_STATE,
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        verbose_name='Property Price',
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to='owner_app.Owner_mod',
        verbose_name='Owner',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    image = models.ForeignKey(
        to=Images_mod,
        on_delete=models.CASCADE
    )



    # Todo , continuar con los campos locatiion, city,



