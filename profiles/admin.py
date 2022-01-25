from django.contrib import admin
from .models import UserProfile


class Profiles(admin.ModelAdmin):
    list_display = (
        'user',
        'default_phone_number',
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode',
        'default_country',
    )

    ordering = ('user'),

# Register your models here.
admin.site.register(UserProfile, Profiles)