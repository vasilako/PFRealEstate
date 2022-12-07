from django.contrib import admin
from django.contrib.auth import get_user_model

from PFRealEstate.user_agent_app.models import UserAgent_mod



UserModel = get_user_model()


@admin.register(UserModel)
class UserAgentAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'email',
    )

    list_filter = (
        'first_name',
        'last_name',
        # 'number_of_properties'
    )



