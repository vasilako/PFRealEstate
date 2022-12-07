from django.contrib import admin

from PFRealEstate.owner_app.models import Owner_mod


# Register your models here.
@admin.register(Owner_mod)
class Owner_modAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'id',
    )

    list_filter = (
        'first_name',
        'last_name',
        'id',
    )