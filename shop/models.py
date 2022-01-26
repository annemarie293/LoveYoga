from django.db import models

# Create your models here.


class ShopProducts(models.Model):

    class Meta:
        verbose_name_plural = 'ShopProducts'

    sku = models.CharField(max_length=254, null=False, blank=False)
    category = models.CharField(max_length=7, null=False, blank=False)
    name = models.CharField(max_length=250, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.name