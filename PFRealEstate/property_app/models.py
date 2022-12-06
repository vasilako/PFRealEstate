from django.db import models
from django.utils.text import slugify
from PFRealEstate.user_agent_app.models import UserAgent_mod


class Images_mod(models.Model):
    filename = models.ImageField(
        upload_to='photos_properties',
    )

    def __str__(self):
        return self.filename


class Location(models.Model):
    name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
    )


class Address(models.Model):
    location = models.ForeignKey(
        to=Location,
        on_delete= models.SET_NULL,
        null=True,
    )

    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        null=True,
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

    title = models.CharField(
        verbose_name='Property Title',
        max_length=200,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        max_length=200,
        editable=False,

    )

    type = models.CharField(
        verbose_name='Property Type',
        max_length=7,
        choices= PROPERTY_TYPES,
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

    location = models.ForeignKey(
        to=Location,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Location'
    )

    city = models.ForeignKey(
        to=City,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name = 'City'
    )

    street_and_number = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Street and number'
    )

    created_by = models.ForeignKey(
        UserAgent_mod,
        on_delete=models.CASCADE
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )
    def __str__(self):
        return f'{self.type} - {self.price} - {self.city} - {self.owner.name} - {self.operation}'

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super().save(*args, **kwargs)




