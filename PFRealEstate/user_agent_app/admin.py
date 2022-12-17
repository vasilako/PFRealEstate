from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth import get_user_model

UserModel = get_user_model()

@admin.register(UserModel)
class UserAgentAdmin(UserAdmin):
    '''
    fieldsets() is for organizate all fields ot the models in custom mode.
    '''
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name','email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('User info'), {'fields': ('phone_number', 'profile_image', 'manage_properties')}),
    )

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
    )

    search_fields = (
        'username',
        'first_name',
        'last_name',
        'phone_number',
        'email',
    )

    ordering = (
        'username',
    )


