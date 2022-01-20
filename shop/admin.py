from django.contrib import admin
from .models import ShopProducts

class ShopProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name'),

# Register your models here.
admin.site.register(ShopProducts, ShopProductsAdmin)