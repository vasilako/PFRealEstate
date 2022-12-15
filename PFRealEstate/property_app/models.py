from django.db import models
from django.utils.text import slugify


class Location_mod(models.Model):
    name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

class City_mod(models.Model):

    city_location = models.ForeignKey(
        to=Location_mod,
        on_delete=models.SET_NULL,
        null=True
    )

    name = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'


class Address_mod(models.Model):

    location = models.ForeignKey(
        to=Location_mod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    city = models.ForeignKey(
        to=City_mod,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    street_and_number = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f'{self.location}, {self.city}, {self.street_and_number}'
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Property_mod(models.Model):
    FLAT = 'flat'
    AREA = 'area'
    CHALET = 'chalet'
    SHOP = 'shop'
    OFFICES = 'offices'

    PROPERTY_TYPES = [
        (FLAT, 'Flat'),
        (AREA, 'Area'),
        (CHALET, 'Chalet'),
        (SHOP, 'Comercial'),
        (OFFICES, 'Offices'),
    ]

    PROPERTY_OPERATION = [
        ('rent', 'Rent'),
        ('buy', 'Buy'),
    ]

    PROPERTY_STATE = [
        ('new', 'New'),
        ('used', 'Used'),
    ]

    operation = models.CharField(
        verbose_name='Operation Type',
        max_length=4,
        choices=PROPERTY_OPERATION,
        null=False,
        blank=False,
    )

    title = models.CharField(
        verbose_name='Property Title',
        max_length=200,
        null=False,
        blank=False,
    )

    type = models.CharField(
        verbose_name='Property Type',
        max_length=7,
        choices=PROPERTY_TYPES,
        null=False,
        blank=False,
    )

    state = models.CharField(
        verbose_name='Property state',
        max_length=4, choices=PROPERTY_STATE,
        null=False,
        blank=False,
    )

    price = models.PositiveIntegerField(
        verbose_name='Property Price',
        null=False,
        blank=False,
    )

    address = models.OneToOneField(
        to=Address_mod,
        on_delete=models.CASCADE,
        verbose_name='Address Property',
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        to='owner_app.Owner_mod',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )

    user_agent = models.ForeignKey(
        to='user_agent_app.UserAgent_mod',
        on_delete=models.SET_NULL,
        null=True,
        blank=False
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
    )
    modified_date = models.DateTimeField(
        auto_now=True,
    )

    slug = models.SlugField(
        max_length=200,
        editable=False,

    )

    def save(self, *args, **kwargs):
        self.slug = slugify(f'id-{self.id}-{self.title}')
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.title}, Type: {self.type}, Price: {self.price} €'



    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'


class Images_mod(models.Model):
    filename = models.ImageField(
        upload_to='photos_properties',
        null=True,
        blank=True,
    )
    to_property = models.ForeignKey(
        to=Property_mod,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.filename)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'