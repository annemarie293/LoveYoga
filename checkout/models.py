import uuid 

from django.db import models
from django.db.models import Sum
from django_countries.fields import CountryField

from shop.models import ShopProducts
from classes.models import YogaClass
from profiles.models import UserProfile
from basket.contexts import basket_contents

# Create your models here.


class Order(models.Model):
    
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name="orders")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    products_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    classes_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default=0)

    def _generate_order_number(self):
        """
        Use UUID to gernerate unique and random 32 digit order reference number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update the order total from the line item values
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.delivery = 0
        if self.products_total != 0:
            self.delivery = 5
        self.grand_total = self.order_total + self.delivery
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the default save to generate the order number if it does not already exist
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    category = models.CharField(max_length=7, null=False, blank=False)
    product = models.ForeignKey(ShopProducts, null=True, blank=True, on_delete=models.CASCADE)
    classes = models.ForeignKey(YogaClass, null=True, blank=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the default save and calculates line item total for each order line
        """
        if self.category == 'product':
            self.lineitem_total = self.product.price * self.quantity
        elif self.category == 'class':
            self.lineitem_total = self.classes.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        if self.category == 'product':
            return f'SKU {self.product.sku} on order {self.order.order_number}'
        elif self.category == 'class':
            return f'SKU {self.classes.sku} on order {self.order.order_number}'