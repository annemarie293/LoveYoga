from django.contrib import admin
from .models import Order, OrderLineItem


# Admin for Order line Item model
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


# Admin for Order model
class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'user_profile',
        'order_number',
        'date',
        'delivery',
        'order_total',
        'grand_total',
        'original_basket',
        'stripe_pid'
    )

    fields = ('user_profile', 'order_number',
              'date', 'full_name',
              'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city',
              'county', 'postcode', 'country',
              'delivery', 'order_total', 'grand_total',
              'original_basket', 'stripe_pid'
              )

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery',
                    'grand_total',)

    ordering = ('-date',)


# Register your models here.

admin.site.register(Order, OrderAdmin)
