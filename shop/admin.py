from django.contrib import admin
from .models import ShopProducts

class ShopProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'class_or_product',
        'image',
    )

    ordering = ('name'),

# Register your models here.
admin.site.register(ShopProducts, ShopProductsAdmin)