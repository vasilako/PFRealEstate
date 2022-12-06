from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin

from PFRealEstate.property_app.models import Property_mod
from PFRealEstate.user_agent_app.models import UserAgent_mod



# Register your models here.
class PropertiesInLine(admin.TabularInline):
    model = Property_mod
    extra = 3


@admin.register(UserAgent_mod)
class UserAgentAdmin(admin.ModelAdmin):

    list_display = (
        # 'first_name',
        # 'last_name',
        'phone_number',
        # 'number_of_properties'
    )

    list_filter = (
        # 'first_name',
        # 'last_name',
        # 'number_of_properties'
    )

    inlines = (
        PropertiesInLine,
    )