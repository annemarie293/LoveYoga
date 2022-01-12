from django.contrib import admin
from .models import YogaClass

class YogaClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'practice',
        'level',
        'intensity',
        'session_duration',
        'series_duration',
        'equipment',
        'trainer',
        'price',
        'image',
    )

    ordering = ('name'),

# Register your models here.
admin.site.register(YogaClass, YogaClassAdmin)