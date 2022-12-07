from django.contrib import admin
from django.contrib.auth import get_user_model
from PFRealEstate.user_agent_app.models import UserAgent_mod


# Register your models here.

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


