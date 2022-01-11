from django.contrib import admin
from .models import Trainer

class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'years_practicing',
        'years_teaching',
        'bio',
        'image'
    )

    ordering = ('name'),

# Register your models here.
admin.site.register(Trainer, TrainerAdmin)