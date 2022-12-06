from django.contrib import admin

from PFRealEstate.owner_app.models import Owner_mod
from PFRealEstate.property_app.models import Property_mod, Location_mod, City_mod, Address_mod


class OwnerInLine(admin.TabularInline):
    model = Owner_mod


@admin.register(Property_mod)
class Property_modAdmin(admin.ModelAdmin):
    list_display = (
        'type',
        'operation',
        'state',
        'price',
        'owner'
    )

    list_filter = (
        'operation',
        'type',
        'price',
        'location',
        'City',
        'title',
        'created_bay'
        'created_date',
        'modified_date'
    )

    inlines = (
        OwnerInLine,
    )


@admin.register(Location_mod)
class Location_modAdmin(admin.ModelAdmin):
    ordering = (
        'name'
    )

    list_display = (
        'name'
    )

@admin.register(City_mod)
class City_modAdmin(admin.ModelAdmin):
    ordering = (
        'name'
    )

    list_display = (
        'name'
    )

@admin.register(Address_mod)
class Address_modAdmin(admin.ModelAdmin):
    list_display = (
        'location',
        'city'
    )