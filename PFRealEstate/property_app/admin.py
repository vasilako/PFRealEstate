from django.contrib import admin

from PFRealEstate.owner_app.models import Owner_mod
from PFRealEstate.property_app.models import Property_mod, Location_mod, City_mod, Address_mod, Images_mod
from PFRealEstate.user_agent_app.models import UserAgent_mod


class ImageInLine(admin.TabularInline):
    model = Images_mod
    extra = 1


@admin.register(Property_mod)
class Property_modAdmin(admin.ModelAdmin):
    fields = (
        'operation',
        'title',
        'type',
        'state',
        'price',
        'address',
        'owner',
        'user_agent'

    )

    list_display = (
        'title',
        'type',
        'operation',
        'state',
        'price',
        'owner',
        'created_date',
    )

    list_filter = (
        'operation',
        'type',
        'price',
        'title',
    )

    inlines = (
        ImageInLine,
    )


@admin.register(Location_mod)
class Location_modAdmin(admin.ModelAdmin):

    ordering = (
        'name',
    )

    list_display = (
        'name',
    )

@admin.register(City_mod)
class City_modAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )

    list_display = (
        'name',
    )

@admin.register(Address_mod)
class Address_modAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'city',
        'street_and_number'
    )
    list_filter = (
        'location',
        'city',
    )

@admin.register(Images_mod)
class Image_modAdmin(admin.ModelAdmin):
    list_display = (
        'filename',

    )
