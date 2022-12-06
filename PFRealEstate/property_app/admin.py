from django.contrib import admin

from PFRealEstate.owner_app.models import Owner_mod
from PFRealEstate.property_app.models import Property_mod, Location_mod, City_mod, Address_mod, Images_mod
from PFRealEstate.user_agent_app.models import UserAgent_mod


class OwnerInLine(admin.TabularInline):
    model = Owner_mod
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
        'owner'
        'created_by',


    )

    list_display = (
        'type',
        'operation',
        'state',
        'price',
    )

    list_filter = (
        'operation',
        'type',
        'price',
        'title',
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
    )

@admin.register(Images_mod)
class Image_modAdmin(admin.ModelAdmin):
    list_display = (
        'filename',

    )
