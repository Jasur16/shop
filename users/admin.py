from django.contrib import admin
from .models import ProfileModel


@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name']
    readonly_fields = ['user', 'first_name', 'last_name', 'email', 'phone', 'country', 'address1', 'address2', 'city',
                       'state', 'zip_code', ]
