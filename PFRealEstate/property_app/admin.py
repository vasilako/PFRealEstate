from django.contrib import admin

from PFRealEstate.owner_app.models import Owner_mod
from PFRealEstate.property_app.models import Property_mod


class OwnerInLine(admin.TabularInline):
    model = Owner_mod
@admin.register(Property_mod)
class Property_modAdmin(admin.ModelAdmin):
    list_display = ('type', 'operation', 'state', 'price', 'owner')
    list_filter = ('type', 'price', 'location', 'operation', 'location')

    inlines = (OwnerInLine)