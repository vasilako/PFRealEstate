from django.contrib import admin

from PFRealEstate.property_app.models import Property_mod
from PFRealEstate.user_agent_app.models import UserAgent_mod



# Register your models here.
class PropertiesInLine:
    model = Property_mod


@admin.register(UserAgent_mod)
class UserAgentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'phone_number'
        'number_of_properties'
    )

    list_filter = (
        'first_name',
        'last_name',
        'number_of_properties'
    )

    inlines = (
        PropertiesInLine,
    )